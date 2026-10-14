# Phase 8E: display-path icon art, derived from the 8D generator (same stdlib
# PNG codec + box-filter resampling, same master, no crop/recolor/redesign).
# Targets are the resources the OS/app actually displays:
#   - res/drawable-nodpi/gold_motion_launcher.png (576x576, manifest icon/roundIcon
#     via @drawable/gold_motion_icon)
#   - res/drawable-nodpi/gold_motion_logo_splash.png (1024x1024, splash theme icon
#     via Theme.App.Starting -> gold_motion_splash_icon layer-list)
import struct, zlib, os
SRC = '/sdcard/Pictures/file_00000000036c81fb8f325767890b4bcb.png'
raw = open(SRC, 'rb').read()
pos = 8; W = H = None; idat = b''
while pos < len(raw):
    ln = struct.unpack('>I', raw[pos:pos+4])[0]
    typ = raw[pos+4:pos+8]; dat = raw[pos+8:pos+8+ln]
    if typ == b'IHDR':
        W, H, bd, ct, _, _, _ = struct.unpack('>IIBBBBB', dat)
        assert (bd, ct) == (8, 2), (bd, ct)
    elif typ == b'IDAT':
        idat += dat
    pos += 12 + ln
print('master', W, 'x', H)
px = zlib.decompress(idat)
stride = W * 3 + 1
rows = []
prev = bytearray(W * 3)
for i in range(H):
    f = px[i * stride]
    cur = bytearray(px[i * stride + 1:(i + 1) * stride])
    if f == 1:
        for j in range(3, len(cur)):
            cur[j] = (cur[j] + cur[j - 3]) & 0xff
    elif f == 2:
        for j in range(len(cur)):
            cur[j] = (cur[j] + prev[j]) & 0xff
    elif f == 3:
        for j in range(len(cur)):
            a = cur[j - 3] if j >= 3 else 0
            cur[j] = (cur[j] + ((a + prev[j]) >> 1)) & 0xff
    elif f == 4:
        for j in range(len(cur)):
            a = cur[j - 3] if j >= 3 else 0
            b = prev[j]
            c = prev[j - 3] if j >= 3 else 0
            p = a + b - c
            pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
            pr = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
            cur[j] = (cur[j] + pr) & 0xff
    elif f != 0:
        raise ValueError(f'unknown filter {f}')
    rows.append(bytes(cur))
    prev = cur
def sample_box(x0, y0, x1, y1):
    r = g = b = n = 0
    for yy in range(y0, y1):
        row = rows[yy]
        for xx in range(x0, x1):
            o = xx * 3
            r += row[o]; g += row[o+1]; b += row[o+2]; n += 1
    return (r // n, g // n, b // n) if n else (0, 0, 0)
def resample(dst):
    out = bytearray()
    for y in range(dst):
        out += b'\x00'
        ay0 = int(H * y / dst); ay1 = int(H * (y + 1) / dst)
        for x in range(dst):
            ax0 = int(W * x / dst); ax1 = int(W * (x + 1) / dst)
            r, g, b = sample_box(max(ax0, 0), max(ay0, 0), min(ax1, W), min(ay1, H))
            out += bytes((r, g, b))
    return bytes(out)
def write_png(path, size, raw_rgb):
    def chunk(t, d):
        c = t + d
        return struct.pack('>I', len(d)) + c + struct.pack('>I', zlib.crc32(c) & 0xffffffff)
    open(path, 'wb').write(b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', size, size, 8, 2, 0, 0, 0)) + chunk(b'IDAT', zlib.compress(raw_rgb)) + chunk(b'IEND', b''))
OUT = os.path.dirname(os.path.abspath(__file__))
for name, size in [('gold_motion_launcher.png', 576), ('gold_motion_logo_splash.png', 1024)]:
    write_png(f'{OUT}/{name}', size, resample(size))
    print(name, os.path.getsize(f'{OUT}/{name}'))
