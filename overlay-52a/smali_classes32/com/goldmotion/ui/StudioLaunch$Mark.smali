# BE52: premium ambient animation (halo ping + ring breathing) over the original reveal
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
