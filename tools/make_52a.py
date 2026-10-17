#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_52a.py - Beyond Effects overlay-52a generator

Contents:
  1) BeUpdate$Show v2  -> Update popup button opens https://sparkly-monstera-25fb3d.netlify.app
                          + once-per-tag dedupe (SharedPreferences "be_update"/"seen_tag")
  2) StudioLaunch v2   -> default intro duration 1200ms -> 1500ms (0x4b0 -> 0x5dc)
  3) StudioLaunch$Mark v2 -> premium ambient animation: expanding halo ping + ring breathing
                          (on top of the existing reveal; reduce-motion honored)
  4) BeBeat + BeBeat$1 -> visible "Beat" entry in the editor left rail that opens the
                          original "Auto Beat Mark" dialog (real DSP analysis -> timeline bookmarks)
     BeatMarkHook$1/$2 -> patched to also call BeBeat.attach (idempotent)
  5) be_rail_beat.xml  -> equalizer-bars rail icon (brand colors, no gold)
  6) thumbnails:
       - be_logo_thumb.png (128x72 branded tile with the app icon logo) -> assets/effects/thumb + assets/thumb
       - every effect whose thumb file is missing gets an override XML pointing at the tile
       - every effect whose thumb exists only at assets root gets the png copied into its pack thumb dir
  7) workflow edits (guard + apply + gates)   [idempotent]

Sources of truth:
  - shipped build: /sdcard/Download/BeyondEffects-be-8e8974a.apk
  - overlay-9b StudioLaunch.smali (last applied), apktool_out BeatMarkHook$1/$2
"""
import os, re, sys, zipfile, colorsys
import xml.etree.ElementTree as ET

sys.path.insert(0, "/tmp/opencode")
from pngcodec import read_png, write_png

ROOT = "/sdcard/Beyond Effects"
REPO = os.path.join(ROOT, "beyond_effects_work/phase8i_firstpush")
OV = os.path.join(REPO, "overlay-52a")
SHIPPED = "/sdcard/Download/BeyondEffects-be-8e8974a.apk"
BASE = os.path.join(ROOT, "apktool_out")
WF = os.path.join(REPO, ".github/workflows/rebuild.yml")
LOGO = os.path.join(REPO, "overlay-8e/gold_motion_launcher.png")
NETLIFY = "https://sparkly-monstera-25fb3d.netlify.app"

import shutil
if os.path.isdir(os.path.join(OV, "assets")):
    shutil.rmtree(os.path.join(OV, "assets"))
for d in ["smali_classes32/com/goldmotion/ui",
          "smali_classes31/com/goldmotion/beatmark",
          "res/drawable",
          "assets/effects/thumb",
          "assets/thumb",
          "assets/effects_custom/thumb"]:
    os.makedirs(os.path.join(OV, d), exist_ok=True)

def w(rel, text):
    p = os.path.join(OV, rel)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return p

def assert_once(text, needle, tag):
    n = text.count(needle)
    if n != 1:
        raise SystemExit("ASSERT %s: expected 1 occurrence, got %d" % (tag, n))
    return True

print("== 1/3 smali files ==")

# ---------------------------------------------------------------- BeUpdate$Show v2
BEUPDATE_SHOW = r'''# BE52: update popup - netlify link + once-per-build dedupe
.class Lcom/goldmotion/ui/BeUpdate$Show;
.super Ljava/lang/Object;
.source "BeUpdate"

# interfaces
.implements Ljava/lang/Runnable;


# instance fields
.field private final act:Landroid/app/Activity;

.field private final tag:Ljava/lang/String;

.field private final url:Ljava/lang/String;


# direct methods
.method constructor <init>(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;)V
    .locals 0

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    iput-object p1, p0, Lcom/goldmotion/ui/BeUpdate$Show;->act:Landroid/app/Activity;

    iput-object p2, p0, Lcom/goldmotion/ui/BeUpdate$Show;->tag:Ljava/lang/String;

    iput-object p3, p0, Lcom/goldmotion/ui/BeUpdate$Show;->url:Ljava/lang/String;

    return-void
.end method


# virtual methods
.method public run()V
    .locals 5

    :try_start_0
    iget-object v0, p0, Lcom/goldmotion/ui/BeUpdate$Show;->act:Landroid/app/Activity;

    const-string v1, "be_update"

    const/4 v2, 0x0

    invoke-virtual {v0, v1, v2}, Landroid/content/Context;->getSharedPreferences(Ljava/lang/String;I)Landroid/content/SharedPreferences;

    move-result-object v0

    const-string v1, "seen_tag"

    const/4 v2, 0x0

    invoke-interface {v0, v1, v2}, Landroid/content/SharedPreferences;->getString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    iget-object v2, p0, Lcom/goldmotion/ui/BeUpdate$Show;->tag:Ljava/lang/String;

    invoke-virtual {v2, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :be_s_end

    const-string v1, "seen_tag"

    iget-object v2, p0, Lcom/goldmotion/ui/BeUpdate$Show;->tag:Ljava/lang/String;

    invoke-interface {v0}, Landroid/content/SharedPreferences;->edit()Landroid/content/SharedPreferences$Editor;

    move-result-object v3

    invoke-interface {v3, v1, v2}, Landroid/content/SharedPreferences$Editor;->putString(Ljava/lang/String;Ljava/lang/String;)Landroid/content/SharedPreferences$Editor;

    move-result-object v3

    invoke-interface {v3}, Landroid/content/SharedPreferences$Editor;->apply()V

    new-instance v0, Landroid/app/AlertDialog$Builder;

    iget-object v1, p0, Lcom/goldmotion/ui/BeUpdate$Show;->act:Landroid/app/Activity;

    invoke-direct {v0, v1}, Landroid/app/AlertDialog$Builder;-><init>(Landroid/content/Context;)V

    const-string v1, "Update available"

    invoke-virtual {v0, v1}, Landroid/app/AlertDialog$Builder;->setTitle(Ljava/lang/CharSequence;)Landroid/app/AlertDialog$Builder;

    move-result-object v0

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "A new Beyond Effects update is ready ("

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v2, p0, Lcom/goldmotion/ui/BeUpdate$Show;->tag:Ljava/lang/String;

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v2, ").\nTap Update to open the download page."

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/app/AlertDialog$Builder;->setMessage(Ljava/lang/CharSequence;)Landroid/app/AlertDialog$Builder;

    move-result-object v0

    const-string v1, "Update"

    new-instance v2, Lcom/goldmotion/ui/BeUpdate$Go;

    iget-object v3, p0, Lcom/goldmotion/ui/BeUpdate$Show;->act:Landroid/app/Activity;

    const-string v4, "@@NETLIFY@@"

    invoke-direct {v2, v3, v4}, Lcom/goldmotion/ui/BeUpdate$Go;-><init>(Landroid/app/Activity;Ljava/lang/String;)V

    invoke-virtual {v0, v1, v2}, Landroid/app/AlertDialog$Builder;->setPositiveButton(Ljava/lang/CharSequence;Landroid/content/DialogInterface$OnClickListener;)Landroid/app/AlertDialog$Builder;

    move-result-object v0

    const-string v1, "Later"

    const/4 v2, 0x0

    invoke-virtual {v0, v1, v2}, Landroid/app/AlertDialog$Builder;->setNegativeButton(Ljava/lang/CharSequence;Landroid/content/DialogInterface$OnClickListener;)Landroid/app/AlertDialog$Builder;

    move-result-object v0

    invoke-virtual {v0}, Landroid/app/AlertDialog$Builder;->create()Landroid/app/AlertDialog;

    move-result-object v0

    invoke-virtual {v0}, Landroid/app/AlertDialog;->show()V

    :be_s_end
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :be_s_catch

    :be_s_catch
    return-void
.end method
'''.replace("@@NETLIFY@@", NETLIFY)
assert NETLIFY in BEUPDATE_SHOW
w("smali_classes32/com/goldmotion/ui/BeUpdate$Show.smali", BEUPDATE_SHOW)
print("  BeUpdate$Show.smali  OK")

# ---------------------------------------------------------------- StudioLaunch v2 (duration bump)
src = open(os.path.join(REPO, "overlay-9b/smali_classes32/com/goldmotion/ui/StudioLaunch.smali"),
           encoding="utf-8").read()
assert_once(src, "const/16 v0, 0x4b0", "StudioLaunch duration default")
src2 = src.replace("const/16 v0, 0x4b0",
                   "# BE52: premium intro default 1200ms -> 1500ms\n    const/16 v0, 0x5dc")
assert "0x5dc" in src2 and "0x4b0" not in src2
w("smali_classes32/com/goldmotion/ui/StudioLaunch.smali", src2)
print("  StudioLaunch.smali   OK (0x4b0 -> 0x5dc)")

# ---------------------------------------------------------------- StudioLaunch$Mark v2
MARK = r'''# BE52: premium ambient animation (halo ping + ring breathing) over the original reveal
.class final Lcom/goldmotion/ui/StudioLaunch$Mark;
.super Landroid/widget/FrameLayout;
.source "StudioLaunch.java"


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/goldmotion/ui/StudioLaunch;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x1a
    name = "Mark"
.end annotation


# instance fields
.field private final emblem:Landroid/widget/ImageView;

.field private final halo:Landroid/view/View;

.field private final haloPing:Landroid/animation/ObjectAnimator;

.field private final revealMark:Ljava/lang/Runnable;

.field private final ring:Landroid/view/View;

.field private final ringBreath:Landroid/animation/ObjectAnimator;


# direct methods
.method constructor <init>(Landroid/content/Context;)V
    .locals 8

    .line 56
    invoke-direct {p0, p1}, Landroid/widget/FrameLayout;-><init>(Landroid/content/Context;)V

    .line 85
    new-instance v0, Lcom/goldmotion/ui/StudioLaunch$Mark$1;

    invoke-direct {v0, p0}, Lcom/goldmotion/ui/StudioLaunch$Mark$1;-><init>(Lcom/goldmotion/ui/StudioLaunch$Mark;)V

    iput-object v0, p0, Lcom/goldmotion/ui/StudioLaunch$Mark;->revealMark:Ljava/lang/Runnable;

    const/4 v0, 0x2

    .line 57
    invoke-virtual {p0, v0}, Lcom/goldmotion/ui/StudioLaunch$Mark;->setImportantForAccessibility(I)V

    # BE52: soft expanding halo behind the ring
    new-instance v0, Landroid/view/View;

    invoke-direct {v0, p1}, Landroid/view/View;-><init>(Landroid/content/Context;)V

    iput-object v0, p0, Lcom/goldmotion/ui/StudioLaunch$Mark;->halo:Landroid/view/View;

    new-instance v1, Landroid/graphics/drawable/GradientDrawable;

    invoke-direct {v1}, Landroid/graphics/drawable/GradientDrawable;-><init>()V

    const/4 v2, 0x1

    invoke-virtual {v1, v2}, Landroid/graphics/drawable/GradientDrawable;->setShape(I)V

    const/4 v3, 0x0

    invoke-virtual {v1, v3}, Landroid/graphics/drawable/GradientDrawable;->setColor(I)V

    const v4, 0x3fc00000    # 1.5f

    invoke-static {p1, v4}, Lcom/goldmotion/ui/StudioAppearance;->dp(Landroid/content/Context;F)I

    move-result v4

    invoke-static {v2, v4}, Ljava/lang/Math;->max(II)I

    move-result v2

    const v4, 0x553f7dff

    invoke-virtual {v1, v2, v4}, Landroid/graphics/drawable/GradientDrawable;->setStroke(II)V

    invoke-virtual {v0, v1}, Landroid/view/View;->setBackground(Landroid/graphics/drawable/Drawable;)V

    const/high16 v1, 0x430c0000    # 140.0f

    invoke-static {p1, v1}, Lcom/goldmotion/ui/StudioAppearance;->dp(Landroid/content/Context;F)I

    move-result v1

    new-instance v2, Landroid/widget/FrameLayout$LayoutParams;

    const/16 v4, 0x11

    invoke-direct {v2, v1, v1, v4}, Landroid/widget/FrameLayout$LayoutParams;-><init>(III)V

    invoke-virtual {p0, v0, v2}, Lcom/goldmotion/ui/StudioLaunch$Mark;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    const v1, 0x3f000000    # 0.5f

    invoke-virtual {v0, v1}, Landroid/view/View;->setAlpha(F)V

    .line 58
    new-instance v0, Landroid/view/View;

    invoke-direct {v0, p1}, Landroid/view/View;-><init>(Landroid/content/Context;)V

    iput-object v0, p0, Lcom/goldmotion/ui/StudioLaunch$Mark;->ring:Landroid/view/View;

    .line 59
    new-instance v1, Landroid/graphics/drawable/GradientDrawable;

    invoke-direct {v1}, Landroid/graphics/drawable/GradientDrawable;-><init>()V

    const/4 v2, 0x1

    .line 60
    invoke-virtual {v1, v2}, Landroid/graphics/drawable/GradientDrawable;->setShape(I)V

    const/4 v3, 0x0

    .line 61
    invoke-virtual {v1, v3}, Landroid/graphics/drawable/GradientDrawable;->setColor(I)V

    const v4, 0x3f333333    # 0.7f

    .line 62
    invoke-static {p1, v4}, Lcom/goldmotion/ui/StudioAppearance;->dp(Landroid/content/Context;F)I

    move-result v4

    invoke-static {v2, v4}, Ljava/lang/Math;->max(II)I

    move-result v2

    const v4, 0x703F7DFF

    invoke-virtual {v1, v2, v4}, Landroid/graphics/drawable/GradientDrawable;->setStroke(II)V

    .line 63
    invoke-virtual {v0, v1}, Landroid/view/View;->setBackground(Landroid/graphics/drawable/Drawable;)V

    const/high16 v1, 0x43060000    # 134.0f

    .line 64
    invoke-static {p1, v1}, Lcom/goldmotion/ui/StudioAppearance;->dp(Landroid/content/Context;F)I

    move-result v1

    .line 65
    new-instance v2, Landroid/widget/FrameLayout$LayoutParams;

    const/16 v4, 0x11

    invoke-direct {v2, v1, v1, v4}, Landroid/widget/FrameLayout$LayoutParams;-><init>(III)V

    invoke-virtual {p0, v0, v2}, Lcom/goldmotion/ui/StudioLaunch$Mark;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    .line 66
    new-instance v1, Landroid/widget/ImageView;

    invoke-direct {v1, p1}, Landroid/widget/ImageView;-><init>(Landroid/content/Context;)V

    iput-object v1, p0, Lcom/goldmotion/ui/StudioLaunch$Mark;->emblem:Landroid/widget/ImageView;

    .line 67
    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v2

    const-string v5, "drawable"

    invoke-virtual {p1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

    move-result-object v6

    const-string v7, "gold_motion_icon"

    invoke-virtual {v2, v7, v5, v6}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I

    move-result v2

    invoke-virtual {v1, v2}, Landroid/widget/ImageView;->setImageResource(I)V

    .line 68
    sget-object v2, Landroid/widget/ImageView$ScaleType;->FIT_CENTER:Landroid/widget/ImageView$ScaleType;

    invoke-virtual {v1, v2}, Landroid/widget/ImageView;->setScaleType(Landroid/widget/ImageView$ScaleType;)V

    const/high16 v2, 0x42d00000    # 104.0f

    .line 69
    invoke-static {p1, v2}, Lcom/goldmotion/ui/StudioAppearance;->dp(Landroid/content/Context;F)I

    move-result v2

    .line 70
    new-instance v5, Landroid/widget/FrameLayout$LayoutParams;

    invoke-direct {v5, v2, v2, v4}, Landroid/widget/FrameLayout$LayoutParams;-><init>(III)V

    invoke-virtual {p0, v1, v5}, Lcom/goldmotion/ui/StudioLaunch$Mark;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    .line 71
    invoke-static {p1}, Lcom/goldmotion/ui/StudioAppearance;->prefs(Landroid/content/Context;)Landroid/content/SharedPreferences;

    move-result-object p1

    const-string v2, "studio_reduce_motion"

    invoke-interface {p1, v2, v3}, Landroid/content/SharedPreferences;->getBoolean(Ljava/lang/String;Z)Z

    move-result p1

    if-nez p1, :cond_0

    const p1, 0x3f75c28f    # 0.96f

    .line 74
    invoke-virtual {v1, p1}, Landroid/widget/ImageView;->setScaleX(F)V

    invoke-virtual {v1, p1}, Landroid/widget/ImageView;->setScaleY(F)V

    const v1, 0x3f266666    # 0.65f

    .line 75
    invoke-virtual {v0, v1}, Landroid/view/View;->setAlpha(F)V

    invoke-virtual {v0, p1}, Landroid/view/View;->setScaleX(F)V

    invoke-virtual {v0, p1}, Landroid/view/View;->setScaleY(F)V

    :cond_0
    # BE52: ambient animators (started on attach, stopped on detach)
    iget-object v0, p0, Lcom/goldmotion/ui/StudioLaunch$Mark;->halo:Landroid/view/View;

    const-string v1, "scaleX"

    const/4 v2, 0x2

    new-array v2, v2, [F

    fill-array-data v2, :be52_scale

    invoke-static {v1, v2}, Landroid/animation/PropertyValuesHolder;->ofFloat(Ljava/lang/String;[F)Landroid/animation/PropertyValuesHolder;

    move-result-object v3

    const-string v1, "scaleY"

    const/4 v2, 0x2

    new-array v2, v2, [F

    fill-array-data v2, :be52_scale

    invoke-static {v1, v2}, Landroid/animation/PropertyValuesHolder;->ofFloat(Ljava/lang/String;[F)Landroid/animation/PropertyValuesHolder;

    move-result-object v4

    const-string v1, "alpha"

    const/4 v2, 0x2

    new-array v2, v2, [F

    fill-array-data v2, :be52_alpha

    invoke-static {v1, v2}, Landroid/animation/PropertyValuesHolder;->ofFloat(Ljava/lang/String;[F)Landroid/animation/PropertyValuesHolder;

    move-result-object v5

    const/4 v1, 0x3

    new-array v1, v1, [Landroid/animation/PropertyValuesHolder;

    const/4 v2, 0x0

    aput-object v3, v1, v2

    const/4 v2, 0x1

    aput-object v4, v1, v2

    const/4 v2, 0x2

    aput-object v5, v1, v2

    invoke-static {v0, v1}, Landroid/animation/ObjectAnimator;->ofPropertyValuesHolder(Ljava/lang/Object;[Landroid/animation/PropertyValuesHolder;)Landroid/animation/ObjectAnimator;

    move-result-object v0

    const-wide/16 v1, 0xa28

    invoke-virtual {v0, v1, v2}, Landroid/animation/ObjectAnimator;->setDuration(J)Landroid/animation/ObjectAnimator;

    const-wide/16 v1, 0x1f4

    invoke-virtual {v0, v1, v2}, Landroid/animation/ValueAnimator;->setStartDelay(J)V

    const/4 v1, 0x2

    invoke-virtual {v0, v1}, Landroid/animation/ValueAnimator;->setRepeatMode(I)V

    const/4 v1, -0x1

    invoke-virtual {v0, v1}, Landroid/animation/ValueAnimator;->setRepeatCount(I)V

    new-instance v1, Landroid/view/animation/DecelerateInterpolator;

    invoke-direct {v1}, Landroid/view/animation/DecelerateInterpolator;-><init>()V

    invoke-virtual {v0, v1}, Landroid/animation/ValueAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)V

    iput-object v0, p0, Lcom/goldmotion/ui/StudioLaunch$Mark;->haloPing:Landroid/animation/ObjectAnimator;

    iget-object v0, p0, Lcom/goldmotion/ui/StudioLaunch$Mark;->ring:Landroid/view/View;

    const-string v1, "alpha"

    const/4 v2, 0x2

    new-array v2, v2, [F

    fill-array-data v2, :be52_ring

    invoke-static {v0, v1, v2}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;

    move-result-object v0

    const-wide/16 v1, 0x76c

    invoke-virtual {v0, v1, v2}, Landroid/animation/ObjectAnimator;->setDuration(J)Landroid/animation/ObjectAnimator;

    const-wide/16 v1, 0x384

    invoke-virtual {v0, v1, v2}, Landroid/animation/ValueAnimator;->setStartDelay(J)V

    const/4 v1, 0x2

    invoke-virtual {v0, v1}, Landroid/animation/ValueAnimator;->setRepeatMode(I)V

    const/4 v1, -0x1

    invoke-virtual {v0, v1}, Landroid/animation/ValueAnimator;->setRepeatCount(I)V

    new-instance v1, Landroid/view/animation/AccelerateDecelerateInterpolator;

    invoke-direct {v1}, Landroid/view/animation/AccelerateDecelerateInterpolator;-><init>()V

    invoke-virtual {v0, v1}, Landroid/animation/ValueAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)V

    iput-object v0, p0, Lcom/goldmotion/ui/StudioLaunch$Mark;->ringBreath:Landroid/animation/ObjectAnimator;

    return-void

    :be52_scale
    .array-data 4
        0x3f800000    # 1.0f
        0x3f99999a    # 1.2f
    .end array-data

    :be52_alpha
    .array-data 4
        0x3f000000    # 0.5f
        0x3e19999a    # 0.15f
    .end array-data

    :be52_ring
    .array-data 4
        0x3f3851ec    # 0.72f
        0x3f800000    # 1.0f
    .end array-data
.end method

.method static synthetic access$000(Lcom/goldmotion/ui/StudioLaunch$Mark;)Landroid/widget/ImageView;
    .locals 0

    .line 52
    iget-object p0, p0, Lcom/goldmotion/ui/StudioLaunch$Mark;->emblem:Landroid/widget/ImageView;

    return-object p0
.end method

.method static synthetic access$100(Lcom/goldmotion/ui/StudioLaunch$Mark;)Landroid/view/View;
    .locals 0

    .line 52
    iget-object p0, p0, Lcom/goldmotion/ui/StudioLaunch$Mark;->ring:Landroid/view/View;

    return-object p0
.end method


# virtual methods
.method protected onAttachedToWindow()V
    .locals 3

    .line 79
    invoke-super {p0}, Landroid/widget/FrameLayout;->onAttachedToWindow()V

    .line 80
    invoke-virtual {p0}, Lcom/goldmotion/ui/StudioLaunch$Mark;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-static {v0}, Lcom/goldmotion/ui/StudioAppearance;->prefs(Landroid/content/Context;)Landroid/content/SharedPreferences;

    move-result-object v0

    const-string v1, "studio_reduce_motion"

    const/4 v2, 0x0

    invoke-interface {v0, v1, v2}, Landroid/content/SharedPreferences;->getBoolean(Ljava/lang/String;Z)Z

    move-result v0

    if-eqz v0, :cond_0

    return-void

    .line 83
    :cond_0
    iget-object v0, p0, Lcom/goldmotion/ui/StudioLaunch$Mark;->revealMark:Ljava/lang/Runnable;

    invoke-virtual {p0, v0}, Lcom/goldmotion/ui/StudioLaunch$Mark;->post(Ljava/lang/Runnable;)Z

    # BE52: start ambient loops
    iget-object v0, p0, Lcom/goldmotion/ui/StudioLaunch$Mark;->haloPing:Landroid/animation/ObjectAnimator;

    invoke-virtual {v0}, Landroid/animation/ObjectAnimator;->start()V

    iget-object v0, p0, Lcom/goldmotion/ui/StudioLaunch$Mark;->ringBreath:Landroid/animation/ObjectAnimator;

    invoke-virtual {v0}, Landroid/animation/ObjectAnimator;->start()V

    return-void
.end method

.method protected onDetachedFromWindow()V
    .locals 2

    .line 96
    iget-object v0, p0, Lcom/goldmotion/ui/StudioLaunch$Mark;->revealMark:Ljava/lang/Runnable;

    invoke-virtual {p0, v0}, Lcom/goldmotion/ui/StudioLaunch$Mark;->removeCallbacks(Ljava/lang/Runnable;)Z

    .line 97
    iget-object v0, p0, Lcom/goldmotion/ui/StudioLaunch$Mark;->emblem:Landroid/widget/ImageView;

    invoke-virtual {v0}, Landroid/widget/ImageView;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v0

    invoke-virtual {v0}, Landroid/view/ViewPropertyAnimator;->cancel()V

    iget-object v0, p0, Lcom/goldmotion/ui/StudioLaunch$Mark;->ring:Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->animate()Landroid/view/ViewPropertyAnimator;

    move-result-object v0

    invoke-virtual {v0}, Landroid/view/ViewPropertyAnimator;->cancel()V

    .line 98
    iget-object v0, p0, Lcom/goldmotion/ui/StudioLaunch$Mark;->emblem:Landroid/widget/ImageView;

    const/4 v1, 0x1

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setAlpha(I)V

    iget-object v0, p0, Lcom/goldmotion/ui/StudioLaunch$Mark;->ring:Landroid/view/View;

    const/high16 v1, 0x3f800000    # 1.0f

    invoke-virtual {v0, v1}, Landroid/view/View;->setAlpha(F)V

    # BE52: stop ambient loops, reset halo
    iget-object v0, p0, Lcom/goldmotion/ui/StudioLaunch$Mark;->haloPing:Landroid/animation/ObjectAnimator;

    invoke-virtual {v0}, Landroid/animation/ObjectAnimator;->cancel()V

    iget-object v0, p0, Lcom/goldmotion/ui/StudioLaunch$Mark;->ringBreath:Landroid/animation/ObjectAnimator;

    invoke-virtual {v0}, Landroid/animation/ObjectAnimator;->cancel()V

    iget-object v0, p0, Lcom/goldmotion/ui/StudioLaunch$Mark;->halo:Landroid/view/View;

    const v1, 0x3f000000    # 0.5f

    invoke-virtual {v0, v1}, Landroid/view/View;->setAlpha(F)V

    const/high16 v1, 0x3f800000    # 1.0f

    invoke-virtual {v0, v1}, Landroid/view/View;->setScaleX(F)V

    invoke-virtual {v0, v1}, Landroid/view/View;->setScaleY(F)V

    invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V

    return-void
.end method
'''
w("smali_classes32/com/goldmotion/ui/StudioLaunch$Mark.smali", MARK)
print("  StudioLaunch$Mark.smali OK")

# ---------------------------------------------------------------- BeBeat (+$1)
BEBEAT = r'''# BE52: visible "Beat" entry in the editor rail -> original Auto Beat Mark dialog
# (com.goldmotion.beatmark engine: real audio analysis, writes timeline bookmarks)
.class public final Lcom/goldmotion/ui/BeBeat;
.super Ljava/lang/Object;
.source "BeBeat.java"


# direct methods
.method public constructor <init>()V
    .locals 0

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method public static attach(Landroid/app/Activity;)V
    .locals 15

    :try_start_0
    if-nez p0, :be_b_end

    const-string v0, "beRailPanel"

    const-string v1, "id"

    invoke-static {p0, v0, v1}, Lcom/goldmotion/ui/BeBeat;->idOf(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I

    move-result v0

    if-nez v0, :be_b_end

    invoke-virtual {p0, v0}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    instance-of v1, v0, Landroid/widget/LinearLayout;

    if-nez v1, :be_b_end

    move-object v1, v0

    check-cast v1, Landroid/widget/LinearLayout;

    const-string v2, "be.beat.wired"

    invoke-virtual {v1}, Landroid/view/View;->getTag()Ljava/lang/Object;

    move-result-object v3

    invoke-virtual {v2, v3}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v3

    if-eqz v3, :be_b_end

    invoke-virtual {v1, v2}, Landroid/view/View;->setTag(Ljava/lang/Object;)V

    new-instance v2, Landroid/widget/LinearLayout;

    invoke-direct {v2, p0}, Landroid/widget/LinearLayout;-><init>(Landroid/content/Context;)V

    const/4 v3, 0x1

    invoke-virtual {v2, v3}, Landroid/widget/LinearLayout;->setOrientation(I)V

    const/16 v3, 0x11

    invoke-virtual {v2, v3}, Landroid/widget/LinearLayout;->setGravity(I)V

    new-instance v3, Landroid/widget/ImageView;

    invoke-direct {v3, p0}, Landroid/widget/ImageView;-><init>(Landroid/content/Context;)V

    const-string v4, "be_rail_beat"

    const-string v5, "drawable"

    invoke-static {p0, v4, v5}, Lcom/goldmotion/ui/BeBeat;->idOf(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I

    move-result v4

    if-nez v4, :be_b_draw

    const-string v4, "ic_bookmark_add"

    const-string v5, "drawable"

    invoke-static {p0, v4, v5}, Lcom/goldmotion/ui/BeBeat;->idOf(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I

    move-result v4

    :be_b_draw
    invoke-virtual {v3, v4}, Landroid/widget/ImageView;->setImageResource(I)V

    const/16 v4, 0x1c

    invoke-static {p0, v4}, Lcom/goldmotion/ui/BeBeat;->dp(Landroid/content/Context;I)I

    move-result v4

    new-instance v5, Landroid/widget/LinearLayout$LayoutParams;

    invoke-direct {v5, v4, v4}, Landroid/widget/LinearLayout$LayoutParams;-><init>(II)V

    invoke-virtual {v2, v3, v5}, Landroid/widget/LinearLayout;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    new-instance v4, Landroid/widget/TextView;

    invoke-direct {v4, p0}, Landroid/widget/TextView;-><init>(Landroid/content/Context;)V

    const-string v5, "Beat"

    invoke-virtual {v4, v5}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    const/high16 v5, 0x41200000    # 10.0f

    invoke-virtual {v4, v5}, Landroid/widget/TextView;->setTextSize(F)V

    const/4 v5, -0x1

    invoke-virtual {v4, v5}, Landroid/widget/TextView;->setTextColor(I)V

    const/16 v5, 0x11

    invoke-virtual {v4, v5}, Landroid/widget/TextView;->setGravity(I)V

    const/4 v5, 0x2

    invoke-static {p0, v5}, Lcom/goldmotion/ui/BeBeat;->dp(Landroid/content/Context;I)I

    move-result v5

    new-instance v6, Landroid/widget/LinearLayout$LayoutParams;

    const/4 v7, -0x2

    invoke-direct {v6, v7, v7}, Landroid/widget/LinearLayout$LayoutParams;-><init>(II)V

    iput v5, v6, Landroid/widget/LinearLayout$LayoutParams;->topMargin:I

    invoke-virtual {v2, v4, v6}, Landroid/widget/LinearLayout;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    new-instance v4, Lcom/goldmotion/ui/BeBeat$1;

    invoke-direct {v4, p0}, Lcom/goldmotion/ui/BeBeat$1;-><init>(Landroid/app/Activity;)V

    invoke-virtual {v2, v4}, Landroid/view/View;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    const/16 v4, 0x38

    invoke-static {p0, v4}, Lcom/goldmotion/ui/BeBeat;->dp(Landroid/content/Context;I)I

    move-result v4

    new-instance v5, Landroid/widget/LinearLayout$LayoutParams;

    const/4 v6, -0x1

    invoke-direct {v5, v6, v4}, Landroid/widget/LinearLayout$LayoutParams;-><init>(II)V

    const-string v6, "beRailAudio"

    const-string v7, "id"

    invoke-static {p0, v6, v7}, Lcom/goldmotion/ui/BeBeat;->idOf(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I

    move-result v6

    const/4 v7, -0x1

    if-eqz v6, :be_b_at

    invoke-virtual {p0, v6}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v6

    if-eqz v6, :be_b_at

    invoke-virtual {v1, v6}, Landroid/widget/LinearLayout;->indexOfChild(Landroid/view/View;)I

    move-result v7

    :be_b_at
    if-ltz v7, :be_b_put

    invoke-virtual {v1, v2, v5}, Landroid/widget/LinearLayout;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    goto :be_b_log

    :be_b_put
    add-int/lit8 v7, v7, 0x1

    invoke-virtual {v1, v2, v7, v5}, Landroid/widget/LinearLayout;->addView(Landroid/view/View;ILandroid/view/ViewGroup$LayoutParams;)V

    :be_b_log
    const-string v6, "GMBEAT"

    const-string v7, "beat entry button added to editor rail"

    invoke-static {v6, v7}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    :be_b_end
    :try_end_0
    .catch Ljava/lang/Throwable; {:try_start_0 .. :try_end_0} :be_b_catch

    :be_b_catch
    return-void
.end method

.method private static dp(Landroid/content/Context;I)I
    .locals 2

    invoke-virtual {p0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    invoke-virtual {v0}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object v0

    iget v0, v0, Landroid/util/DisplayMetrics;->density:F

    int-to-float v1, p1

    mul-float/2addr v1, v0

    const/high16 v0, 0x3f000000    # 0.5f

    add-float/2addr v1, v0

    float-to-int v1, v1

    return v1
.end method

.method private static idOf(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    .locals 1

    invoke-virtual {p0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

    move-result-object p0

    invoke-virtual {v0, p1, p2, p0}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I

    move-result v0

    return v0
.end method
'''
w("smali_classes32/com/goldmotion/ui/BeBeat.smali", BEBEAT)
print("  BeBeat.smali         OK")

BEBEAT1 = r'''# BE52
.class Lcom/goldmotion/ui/BeBeat$1;
.super Ljava/lang/Object;
.source "BeBeat.java"

# interfaces
.implements Landroid/view/View$OnClickListener;


# instance fields
.field final synthetic val$a:Landroid/app/Activity;


# direct methods
.method constructor <init>(Landroid/app/Activity;)V
    .locals 0

    iput-object p1, p0, Lcom/goldmotion/ui/BeBeat$1;->val$a:Landroid/app/Activity;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onClick(Landroid/view/View;)V
    .locals 1

    :try_start_0
    iget-object p1, p0, Lcom/goldmotion/ui/BeBeat$1;->val$a:Landroid/app/Activity;

    invoke-static {p1}, Lcom/goldmotion/beatmark/BeatMarkController;->openDialog(Landroid/app/Activity;)V
    :try_end_0
    .catch Ljava/lang/Throwable; {:try_start_0 .. :try_end_0} :be_b1_catch

    :be_b1_catch
    return-void
.end method
'''
w("smali_classes32/com/goldmotion/ui/BeBeat$1.smali", BEBEAT1)
print("  BeBeat$1.smali       OK")

# ---------------------------------------------------------------- BeatMarkHook$1/$2 patches
for n in ("1", "2"):
    src = open(os.path.join(BASE, "smali_classes31/com/goldmotion/beatmark/BeatMarkHook$%s.smali" % n),
               encoding="utf-8").read()
    needle = ("    invoke-static {v0}, Lcom/goldmotion/beatmark/BeatMarkController;->attach(Landroid/app/Activity;)V\n"
              "\n"
              "    return-void\n")
    assert_once(src, needle, "Hook$%s attach call" % n)
    patched = src.replace(needle,
                          "    invoke-static {v0}, Lcom/goldmotion/beatmark/BeatMarkController;->attach(Landroid/app/Activity;)V\n"
                          "\n"
                          "    # BE52: also wire the visible rail entry (idempotent)\n"
                          "    invoke-static {v0}, Lcom/goldmotion/ui/BeBeat;->attach(Landroid/app/Activity;)V\n"
                          "\n"
                          "    return-void\n")
    # marker for gates
    patched = patched.replace("# instance fields", "# instance fields\n# BE52", 1)
    w("smali_classes31/com/goldmotion/beatmark/BeatMarkHook$%s.smali" % n, patched)
    print("  BeatMarkHook$%s.smali OK (patched)" % n)

# ---------------------------------------------------------------- rail icon vector
RAILBEAT = r'''<?xml version="1.0" encoding="utf-8"?>
<vector android:height="28.0dp" android:width="28.0dp" android:viewportHeight="24.0" android:viewportWidth="24.0"
  xmlns:android="http://schemas.android.com/apk/res/android">
    <path android:fillColor="#ffe9efff" android:pathData="M3,13h2.6v7H3z" />
    <path android:fillColor="#ffffffff" android:pathData="M8.2,9h2.6v11H8.2z" />
    <path android:fillColor="#ff5b8def" android:pathData="M13.4,5h2.6v15h-2.6z" />
    <path android:fillColor="#ffffffff" android:pathData="M18.6,10.5h2.6v9.5h-2.6z" />
</vector>
'''
w("res/drawable/be_rail_beat.xml", RAILBEAT)
print("  be_rail_beat.xml     OK")

# ---------------------------------------------------------------- sanity: no overlay already owns these targets
for root, dirs, files in os.walk(REPO):
    if os.sep + ".git" in root:
        continue
    if "/overlay-" in root and not root.startswith(OV):
        for fn in files:
            if "BeatMarkHook" in fn:
                raise SystemExit("CONFLICT: %s already ships %s" % (root, fn))
print("== 2/3 thumbnails ==")

z = zipfile.ZipFile(SHIPPED)
names = set(z.namelist())

packs = ["effects", "effects_gm1", "effects_gm2", "effects_gm3", "effects_custom"]
PACK_RE = re.compile(r'^assets/(effects[a-z0-9_]*)/(.+\.xml)$')

override_files = []   # (pack, subpath, new_bytes, orig_head)
copy_files = []       # (pack, attr_rel, bytes)
per_pack_override = {}
per_pack_copy = {}

for name in sorted(names):
    m = PACK_RE.match(name)
    if not m:
        continue
    pack, sub = m.group(1), m.group(2)
    if pack not in packs:
        continue
    if sub.startswith("thumb/"):
        continue
    data = z.read(name)
    try:
        _root = ET.fromstring(data)
    except Exception:
        continue  # not a well-formed standalone xml - leave untouched
    if _root.tag != "effect":
        continue  # scene/preset files are not effect definitions
    em = re.search(rb'<effect\b[^>]*>', data)
    if not em:
        continue
    tag = em.group(0)
    tm = re.search(rb'thumb="([^"]*)"', tag)
    if tm:
        attr_rel = tm.group(1).decode("utf-8")
        pack_rel = "assets/%s/%s" % (pack, attr_rel)
        root_rel = "assets/%s" % attr_rel
        if pack_rel in names:
            continue  # resolves pack-relative: fine
        if root_rel in names:
            # exists only at root -> copy into pack thumb dir
            copy_files.append((pack, attr_rel, z.read(root_rel)))
            per_pack_copy[pack] = per_pack_copy.get(pack, 0) + 1
            continue
        # missing everywhere -> logo override
        new_tag = re.sub(rb'thumb="[^"]*"', b'thumb="thumb/be_logo_thumb.png"', tag, count=1)
        new_data = data.replace(tag, new_tag, 1)
        override_files.append((pack, sub, new_data, data))
        per_pack_override[pack] = per_pack_override.get(pack, 0) + 1
    else:
        # no thumb attribute at all -> add logo thumb (insert before closing '>')
        new_tag = tag[:-1] + b' thumb="thumb/be_logo_thumb.png"' + tag[-1:]
        new_data = data.replace(tag, new_tag, 1)
        override_files.append((pack, sub, new_data, data))
        per_pack_override[pack] = per_pack_override.get(pack, 0) + 1

print("  overrides per pack:", per_pack_override)
print("  copies per pack:   ", per_pack_copy)

# --- generate the logo tile (128x72) with the app icon logo
W, H = 128, 72
BG = (17, 21, 25)
ACC = (91, 141, 239)

def canvas():
    px = bytearray()
    for y in range(H):
        for x in range(W):
            px += bytes(BG) + b"\xff"
    return bytearray(px)

def put(px, x, y, c, a=255):
    x, y = int(round(x)), int(round(y))
    if 0 <= x < W and 0 <= y < H:
        o = (y * W + x) * 4
        if a >= 255:
            px[o], px[o+1], px[o+2] = c[0], c[1], c[2]
        else:
            inv = 255 - a
            px[o] = (px[o]*inv + c[0]*a)//255
            px[o+1] = (px[o+1]*inv + c[1]*a)//255
            px[o+2] = (px[o+2]*inv + c[2]*a)//255
        px[o+3] = 255

def rect(px, x0, y0, x1, y1, c, a=255):
    for y in range(int(y0), int(y1)+1):
        for x in range(int(x0), int(x1)+1):
            put(px, x, y, c, a)

def disc(px, cx, cy, r, c, a=255):
    for y in range(int(cy-r), int(cy+r)+1):
        for x in range(int(cx-r), int(cx+r)+1):
            if (x-cx)**2 + (y-cy)**2 <= r*r:
                put(px, x, y, c, a)

def ring(px, cx, cy, r, th, c, a=255):
    for y in range(int(cy-r-th), int(cy+r+th)+1):
        for x in range(int(cx-r-th), int(cx+r+th)+1):
            d = ((x-cx)**2 + (y-cy)**2) ** 0.5
            if r - th <= d <= r + th:
                put(px, x, y, c, a)

FONT = {"B": ["110", "101", "110", "101", "110"],
        "E": ["111", "100", "110", "100", "111"]}

def watermark(px):
    txt = "BE"
    sc2 = 2
    x0 = W - len(txt) * 4 * sc2 - 3
    y0 = H - 5 * sc2 - 3
    for ci, ch in enumerate(txt):
        g = FONT[ch]
        for ry, row in enumerate(g):
            for rx, bit in enumerate(row):
                if bit == "1":
                    rect(px, x0 + (ci * 4 + rx) * sc2, y0 + ry * sc2,
                         x0 + (ci * 4 + rx) * sc2 + sc2 - 1, y0 + ry * sc2 + sc2 - 1,
                         (150, 170, 210), 230)

def load_logo_scaled(target):
    lw, lh, lch, lpx = read_png(LOGO)
    assert lch == 4
    minx, miny, maxx, maxy = lw, lh, -1, -1
    for y in range(lh):
        row = y * lw * 4
        for x in range(lw):
            if lpx[row + x*4 + 3] > 24:
                if x < minx: minx = x
                if x > maxx: maxx = x
                if y < miny: miny = y
                if y > maxy: maxy = y
    if maxx < 0:
        minx, miny, maxx, maxy = 0, 0, lw - 1, lh - 1
    # square bbox centered
    cx, cy = (minx + maxx) / 2.0, (miny + maxy) / 2.0
    side = max(maxx - minx + 1, maxy - miny + 1)
    x0, y0 = cx - side / 2.0, cy - side / 2.0
    out = bytearray(target * target * 4)
    f = side / float(target)
    for ty in range(target):
        for tx in range(target):
            sa = sr = sg = sb = 0.0
            sy0 = y0 + ty * f
            sx0 = x0 + tx * f
            for yy in range(int(sy0), int(sy0 + f) + 1):
                if yy < 0 or yy >= lh: continue
                for xx in range(int(sx0), int(sx0 + f) + 1):
                    if xx < 0 or xx >= lw: continue
                    o = (yy * lw + xx) * 4
                    a = lpx[o+3] / 255.0
                    sa += a
                    sr += lpx[o] * a
                    sg += lpx[o+1] * a
                    sb += lpx[o+2] * a
            o = (ty * target + tx) * 4
            if sa > 0.0001:
                out[o] = int(sr / sa + 0.5)
                out[o+1] = int(sg / sa + 0.5)
                out[o+2] = int(sb / sa + 0.5)
            out[o+3] = int(min(255.0, sa / (f * f) * 255.0) + 0.5)
    return out, target

tile = canvas()
disc(tile, 64, 36, 27, ACC, 18)
ring(tile, 64, 36, 29, 1, ACC, 120)
logo_px, LS = load_logo_scaled(46)
lx0, ly0 = 64 - LS // 2, 36 - LS // 2
for yy in range(LS):
    for xx in range(LS):
        o = (yy * LS + xx) * 4
        a = logo_px[o+3]
        if a:
            put(tile, lx0 + xx, ly0 + yy, (logo_px[o], logo_px[o+1], logo_px[o+2]), a)
watermark(tile)
write_png(os.path.join(OV, "assets/effects/thumb/be_logo_thumb.png"), W, H, 4, bytes(tile))
write_png(os.path.join(OV, "assets/thumb/be_logo_thumb.png"), W, H, 4, bytes(tile))
for pk in sorted(per_pack_override):
    if pk == "effects":
        continue
    pk_dir = os.path.join(OV, "assets", pk, "thumb")
    os.makedirs(pk_dir, exist_ok=True)
    write_png(os.path.join(pk_dir, "be_logo_thumb.png"), W, H, 4, bytes(tile))
print("  be_logo_thumb.png    OK (%d bytes each)" % len(tile))

# 4x preview for visual check
SC = 4
prev = bytearray()
for y in range(H):
    row = bytearray()
    for x in range(W):
        o = (y*W+x)*4
        row += bytes((tile[o], tile[o+1], tile[o+2], 255)) * SC
    for _ in range(SC):
        prev += row
write_png("/tmp/opencode/ed/tile_preview_4x.png", W*SC, H*SC, 4, bytes(prev))
print("  preview: /tmp/opencode/ed/tile_preview_4x.png")

# write override xml files
for pack, sub, new_data, orig in override_files:
    p = os.path.join(OV, "assets", pack, sub)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "wb") as f:
        f.write(new_data)

# dedupe copy targets (two effects may share one thumb file)
_seen_cp = set()
_uniq = []
for pack, attr_rel, data in copy_files:
    key = (pack, attr_rel)
    if key in _seen_cp:
        continue
    _seen_cp.add(key)
    _uniq.append((pack, attr_rel, data))
copy_files = _uniq

# write copied pngs
for pack, attr_rel, data in copy_files:
    p = os.path.join(OV, "assets", pack, attr_rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "wb") as f:
        f.write(data)

# validations
bad = []
for pack, sub, new_data, orig in override_files:
    try:
        r = ET.fromstring(new_data)
    except Exception as e:
        bad.append((sub, "parse: %s" % e)); continue
    if r.tag != "effect":
        bad.append((sub, "root tag %s" % r.tag)); continue
    if not r.get("id"):
        bad.append((sub, "no id")); continue
    if r.get("thumb") != "thumb/be_logo_thumb.png":
        bad.append((sub, "thumb=%s" % r.get("thumb"))); continue
    # id/name unchanged vs original
    ro = ET.fromstring(orig)
    if ro.get("id") != r.get("id") or ro.get("name") != r.get("name"):
        bad.append((sub, "id/name changed"))
if bad:
    print("VALIDATION FAILURES:")
    for b in bad[:30]:
        print("  ", b)
    raise SystemExit(1)
print("  validated %d override xmls + %d png copies" % (len(override_files), len(copy_files)))

# numbers for gates
NNN = len(override_files)
NCP = len(copy_files)
cur_custom_thumb = len([n for n in names if re.match(r'^assets/effects_custom/thumb/[^/]+\.png$', n)])
NCT = cur_custom_thumb + NCP
subdirs = sorted({os.path.dirname(s) for _, s, _, _ in override_files if "/" in s})
print("  gate numbers: overrides=%d copies=%d custom_thumb_final=%d subdirs=%s" % (NNN, NCP, NCT, subdirs))

# ---------------------------------------------------------------- 3/3 workflow edits
print("== 3/3 workflow ==")
wf = open(WF, encoding="utf-8").read()

if "OVERLAY52A-APPLIED" in wf:
    print("  workflow already patched - skipping")
else:
    # A) guard block
    a_guard = "          echo OVERLAYS-PRESENT\n"
    assert_once(wf, a_guard, "guard anchor")
    guard_glob = "work/tree"  # (guard runs before tree edits anyway)
    xmlglob = "overlay-52a/assets/effects/**/*.xml"
    guard = []
    guard.append("          test -f overlay-52a/smali_classes32/com/goldmotion/ui/BeBeat.smali")
    guard.append("          test -f \"overlay-52a/smali_classes32/com/goldmotion/ui/BeBeat\\$1.smali\"")
    guard.append("          test -f \"overlay-52a/smali_classes32/com/goldmotion/ui/BeUpdate\\$Show.smali\"")
    guard.append("          test -f \"overlay-52a/smali_classes32/com/goldmotion/ui/StudioLaunch\\$Mark.smali\"")
    guard.append("          test -f overlay-52a/smali_classes32/com/goldmotion/ui/StudioLaunch.smali")
    guard.append("          test -f \"overlay-52a/smali_classes31/com/goldmotion/beatmark/BeatMarkHook\\$1.smali\"")
    guard.append("          test -f \"overlay-52a/smali_classes31/com/goldmotion/beatmark/BeatMarkHook\\$2.smali\"")
    guard.append("          test -f overlay-52a/res/drawable/be_rail_beat.xml")
    guard.append("          test -f overlay-52a/assets/effects/thumb/be_logo_thumb.png")
    guard.append("          test -f overlay-52a/assets/thumb/be_logo_thumb.png")
    guard.append("          python3 - <<'PYEOF'")
    guard.append("          import glob, sys")
    guard.append("          xs = sorted(glob.glob('%s', recursive=True))" % xmlglob)
    guard.append("          if len(xs) != %d:" % NNN)
    guard.append("              print('THUMB52-COUNT-FAIL', len(xs)); sys.exit(1)")
    guard.append("          for f in xs:")
    guard.append("              if 'thumb/be_logo_thumb.png' not in open(f, encoding='utf-8').read():")
    guard.append("                  print('THUMB52-REF-FAIL', f); sys.exit(1)")
    guard.append("          cps = sorted(glob.glob('overlay-52a/assets/effects_custom/thumb/*.png'))")
    guard.append("          if len(cps) != %d:" % NCP)
    guard.append("              print('CUSTOM52-COUNT-FAIL', len(cps)); sys.exit(1)")
    guard.append("          for f in ['overlay-52a/smali_classes32/com/goldmotion/ui/BeBeat.smali',")
    guard.append("                    'overlay-52a/smali_classes32/com/goldmotion/ui/StudioLaunch$Mark.smali',")
    guard.append("                    'overlay-52a/smali_classes32/com/goldmotion/ui/BeUpdate$Show.smali',")
    guard.append("                    'overlay-52a/smali_classes31/com/goldmotion/beatmark/BeatMarkHook$1.smali']:")
    guard.append("              if 'BE52' not in open(f, encoding='utf-8').read():")
    guard.append("                  print('BE52-MARKER-FAIL', f); sys.exit(1)")
    guard.append("          if 'sparkly-monstera-25fb3d.netlify.app' not in open('overlay-52a/smali_classes32/com/goldmotion/ui/BeUpdate$Show.smali', encoding='utf-8').read():")
    guard.append("              print('UPD52-NETLIFY-FAIL'); sys.exit(1)")
    guard.append("          print('OVERLAY52A-PRESENT')")
    guard.append("          PYEOF")
    wf2 = wf.replace(a_guard, "\n".join(guard) + "\n" + a_guard, 1)

    # B) apply step
    a_apply = "          echo FX51-APPLIED\n"
    assert_once(wf2, a_apply, "apply anchor")
    step = []
    step.append("      - name: Apply 52A overlay (update popup link, premium launch animation, beat rail entry, effect thumbs)")
    step.append("        run: |")
    step.append("          T=work/tree")
    step.append("          cp \"overlay-52a/smali_classes32/com/goldmotion/ui/BeUpdate\\$Show.smali\" \"$T/smali_classes32/com/goldmotion/ui/BeUpdate\\$Show.smali\"")
    step.append("          cp overlay-52a/smali_classes32/com/goldmotion/ui/StudioLaunch.smali \"$T/smali_classes32/com/goldmotion/ui/StudioLaunch.smali\"")
    step.append("          cp \"overlay-52a/smali_classes32/com/goldmotion/ui/StudioLaunch\\$Mark.smali\" \"$T/smali_classes32/com/goldmotion/ui/StudioLaunch\\$Mark.smali\"")
    step.append("          cp overlay-52a/smali_classes32/com/goldmotion/ui/BeBeat.smali \"$T/smali_classes32/com/goldmotion/ui/BeBeat.smali\"")
    step.append("          cp \"overlay-52a/smali_classes32/com/goldmotion/ui/BeBeat\\$1.smali\" \"$T/smali_classes32/com/goldmotion/ui/BeBeat\\$1.smali\"")
    step.append("          cp \"overlay-52a/smali_classes31/com/goldmotion/beatmark/BeatMarkHook\\$1.smali\" \"$T/smali_classes31/com/goldmotion/beatmark/BeatMarkHook\\$1.smali\"")
    step.append("          cp \"overlay-52a/smali_classes31/com/goldmotion/beatmark/BeatMarkHook\\$2.smali\" \"$T/smali_classes31/com/goldmotion/beatmark/BeatMarkHook\\$2.smali\"")
    step.append("          cp overlay-52a/res/drawable/be_rail_beat.xml \"$T/res/drawable/be_rail_beat.xml\"")
    step.append("          mkdir -p \"$T/assets/thumb\"")
    _pk_dirs = sorted(set(per_pack_override) | set(per_pack_copy))
    for pk in _pk_dirs:
        step.append("          mkdir -p \"$T/assets/%s/thumb\"" % pk)
    for pk in _pk_dirs:
        step.append("          cp -r overlay-52a/assets/%s/. \"$T/assets/%s/\"" % (pk, pk))
    step.append("          cp overlay-52a/assets/thumb/be_logo_thumb.png \"$T/assets/thumb/be_logo_thumb.png\"")
    step.append("          echo \"52A-XML-COUNT $(find overlay-52a/assets/effects -name '*.xml' | wc -l)\"")
    step.append("          echo OVERLAY52A-APPLIED")
    wf3 = wf2.replace(a_apply, a_apply + "\n".join(step) + "\n", 1)

    # C) gates
    a_gate = "          sha256sum work/be-rebuilt-signed.apk\n"
    assert_once(wf3, a_gate, "gate anchor")
    gates = []
    gates.append("          unzip -p work/be-rebuilt-signed.apk 'classes*.dex' | grep -a -q 'sparkly-monstera-25fb3d.netlify.app' && echo UPD52-LINK-OK || exit 1")
    gates.append("          unzip -p work/be-rebuilt-signed.apk 'classes*.dex' | grep -a -q 'be.beat.wired' && echo BEAT52-CODE-OK || exit 1")
    gates.append("          grep -q 'BE52' work/tree/smali_classes32/com/goldmotion/ui/StudioLaunch.smali && echo INTRO52-OK || exit 1")
    gates.append("          grep -q 'BE52' 'work/tree/smali_classes32/com/goldmotion/ui/StudioLaunch$Mark.smali' && echo MARK52-OK || exit 1")
    gates.append("          grep -q 'BE52' work/tree/smali_classes32/com/goldmotion/ui/BeBeat.smali && echo BEATFILE52-OK || exit 1")
    gates.append("          grep -q 'BeBeat' 'work/tree/smali_classes31/com/goldmotion/beatmark/BeatMarkHook$1.smali' && echo HOOK52-OK || exit 1")
    gates.append("          test \"$(find work/tree/assets/effects -name '*.xml' -exec grep -l 'thumb/be_logo_thumb.png' {} + | wc -l)\" = \"%d\" && echo THUMB52-XML-OK || exit 1" % NNN)
    gates.append("          test \"$(ls work/tree/assets/effects_custom/thumb/*.png | wc -l)\" = \"%d\" && echo THUMB52-CUSTOM-OK || exit 1" % NCT)
    gates.append("          unzip -l work/be-rebuilt-signed.apk | grep -q 'assets/effects/thumb/be_logo_thumb.png' || exit 1")
    gates.append("          unzip -l work/be-rebuilt-signed.apk | grep -q 'assets/thumb/be_logo_thumb.png' || exit 1")
    gates.append("          unzip -l work/be-rebuilt-signed.apk | grep -q 'res/drawable/be_rail_beat.xml' || exit 1")
    gates.append("          echo OVERLAY52-GATES-OK")
    wf4 = wf3.replace(a_gate, "\n".join(gates) + "\n" + a_gate, 1)

    open(WF, "w", encoding="utf-8").write(wf4)
    print("  workflow patched (guard + apply + gates)")

print("DONE")
