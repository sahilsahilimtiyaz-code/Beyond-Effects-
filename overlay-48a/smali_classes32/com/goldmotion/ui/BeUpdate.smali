.class public Lcom/goldmotion/ui/BeUpdate;
.super Ljava/lang/Object;
.source "BeUpdate"

.field public static BE_BUILD_TAG:Ljava/lang/String; = "be-BUILD_TAG"

.method public static check(Landroid/app/Activity;)V
    .locals 2

    :try_start_0
    new-instance v0, Ljava/lang/Thread;

    new-instance v1, Lcom/goldmotion/ui/BeUpdate$Fetch;

    invoke-direct {v1, p0}, Lcom/goldmotion/ui/BeUpdate$Fetch;-><init>(Landroid/app/Activity;)V

    invoke-direct {v0, v1}, Ljava/lang/Thread;-><init>(Ljava/lang/Runnable;)V

    invoke-virtual {v0}, Ljava/lang/Thread;->start()V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :be_upd_catch

    :be_upd_catch
    return-void
.end method
