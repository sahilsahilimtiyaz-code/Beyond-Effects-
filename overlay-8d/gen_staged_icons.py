# Phase 8D: faithful downscales of the user's master artwork ONLY.
# No crop, recolor, redesign, or content change. Box-filter resampling.
import struct, zlib
SRC = '/sdcard/Pictures/file_00000000036c81fb8f325767890b4bcb.png'
raw = open(SRC,'rb').read()
pos = 8; W = H = None; chans = None; idat = b''
while pos < len(raw):
    ln = struct.unpack('>I', raw[pos:pos+4])[0]
    typ = raw[pos+4:pos+8]; dat = raw[pos+8:pos+8+ln]
    if typ == b'IHDR':
        W,H,bd,ct,_,_,_ = struct.unpack('>IIBBBBB', dat)
        assert (bd,ct) == (8,2), (bd,ct)
    elif typ == b'IDAT':
        idat += dat
    pos += 12 + ln
print('master', W, 'x', H)
px = zlib.decompress(idat)
stride = W * 3 + 1
# reverse PNG row filters (None/Sub/Up/Average/Paeth)
rows = []
prev = bytearray(W * 3)
for i in range(H):
    f = px[i * stride]
    cur = bytearray(px[i * stride + 1:(i + 1) * stride])
    if f == 1:  # Sub
        for j in range(3, len(cur)):
            cur[j] = (cur[j] + cur[j - 3]) & 0xff
    elif f == 2:  # Up
        for j in range(len(cur)):
            cur[j] = (cur[j] + prev[j]) & 0xff
    elif f == 3:  # Average
        for j in range(len(cur)):
            a = cur[j - 3] if j >= 3 else 0
            cur[j] = (cur[j] + ((a + prev[j]) >> 1)) & 0xff
    elif f == 4:  # Paeth
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
    # average over source rect (integral-image-free direct loop; small targets only)
    r = g = b = n = 0
    for yy in range(y0, y1):
        row = rows[yy]
        for xx in range(x0, x1):
            o = xx * 3
            r += row[o]; g += row[o+1]; b += row[o+2]; n += 1
    return (r // n, g // n, b // n)
def resample(dst, box=None):
    # box = (sx0, sy0, sx1, sy1) source rect mapped onto full dst (default: whole image)
    sx0, sy0, sx1, sy1 = box or (0, 0, W, H)
    out = bytearray()
    for y in range(dst):
        out += b'\x00'
        ay0 = int(sy0 + (sy1 - sy0) * y / dst); ay1 = int(sy0 + (sy1 - sy0) * (y + 1) / dst)
        for x in range(dst):
            ax0 = int(sx0 + (sx1 - sx0) * x / dst); ax1 = int(sx0 + (sx1 - sx0) * (x + 1) / dst)
            r, g, b = sample_box(max(ax0,0), max(ay0,0), min(ax1,W), min(ay1,H))
            out += bytes((r, g, b))
    return bytes(out), dst
def write_png(path, size, raw_rgb):
    def chunk(t, d):
        c = t + d
        return struct.pack('>I', len(d)) + c + struct.pack('>I', zlib.crc32(c) & 0xffffffff)
    open(path, 'wb').write(b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', size, size, 8, 2, 0, 0, 0)) + chunk(b'IDAT', zlib.compress(raw_rgb)) + chunk(b'IEND', b''))
import os
OUT = os.path.dirname(os.path.abspath(__file__))
for name, size in [('be_final_launcher_192.png', 192), ('be_final_launcher_144.png', 144),
                   ('be_final_launcher_96.png', 96), ('be_final_launcher_72.png', 72),
                   ('be_final_launcher_48.png', 48), ('be_final_launcher_round_192.png', 192)]:
    rgb, _ = resample(size)
    write_png(f'{OUT}/{name}', size, rgb)
    print(name, os.path.getsize(f'{OUT}/{name}'))
# adaptive foreground: 432px canvas, artwork scaled into 72dp safe zone (288px),
# transparent surround so the adaptive background shows through unaltered.
S = 432; inner = 288; off = (S - inner) // 2
rgb_inner_raw, _ = resample(inner)
inner_rows = [rgb_inner_raw[y * (inner * 3 + 1) + 1:(y + 1) * (inner * 3 + 1)]
              for y in range(inner)]
rgba = bytearray()
for y in range(S):
    rgba += b'\x00'
    if off <= y < off + inner:
        row = inner_rows[y - off]
        for x in range(S):
            if off <= x < off + inner:
                rgba += row[(x - off) * 3:(x - off) * 3 + 3] + b'\xff'
            else:
                rgba += b'\x00\x00\x00\x00'
    else:
        rgba += b'\x00\x00\x00\x00' * S
def chunk(t, d):
    c = t + d
    return struct.pack('>I', len(d)) + c + struct.pack('>I', zlib.crc32(c) & 0xffffffff)
open(f'{OUT}/be_final_fg_432.png', 'wb').write(b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', S, S, 8, 6, 0, 0, 0)) + chunk(b'IDAT', zlib.compress(bytes(rgba))) + chunk(b'IEND', b''))
print('be_final_fg_432.png', os.path.getsize(f'{OUT}/be_final_fg_432.png'))
