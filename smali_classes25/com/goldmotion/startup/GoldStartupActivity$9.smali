.class Lcom/goldmotion/startup/GoldStartupActivity$9;
.super Ljava/lang/Object;
.source "GoldStartupActivity.java"

# interfaces
.implements Ljava/lang/Runnable;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/goldmotion/startup/GoldStartupActivity;->showLoading()V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/goldmotion/startup/GoldStartupActivity;

.field private bar:Landroid/widget/ProgressBar;

.field private status:Landroid/widget/TextView;

.field private pct:Landroid/widget/TextView;

.field private ticks:I


# direct methods
.method constructor <init>(Lcom/goldmotion/startup/GoldStartupActivity;Landroid/widget/ProgressBar;Landroid/widget/TextView;Landroid/widget/TextView;)V
    .locals 1
    .annotation system Ldalvik/annotation/MethodParameters;
        accessFlags = {
            0x8010,
            0x0,
            0x0,
            0x0
        }
        names = {
            null,
            null,
            null,
            null
        }
    .end annotation

    iput-object p1, p0, Lcom/goldmotion/startup/GoldStartupActivity$9;->this$0:Lcom/goldmotion/startup/GoldStartupActivity;

    iput-object p2, p0, Lcom/goldmotion/startup/GoldStartupActivity$9;->bar:Landroid/widget/ProgressBar;

    iput-object p3, p0, Lcom/goldmotion/startup/GoldStartupActivity$9;->status:Landroid/widget/TextView;

    iput-object p4, p0, Lcom/goldmotion/startup/GoldStartupActivity$9;->pct:Landroid/widget/TextView;

    const/4 v0, 0x0

    iput v0, p0, Lcom/goldmotion/startup/GoldStartupActivity$9;->ticks:I

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .locals 9

    iget-object v0, p0, Lcom/goldmotion/startup/GoldStartupActivity$9;->this$0:Lcom/goldmotion/startup/GoldStartupActivity;

    if-eqz v0, :cond_done

    invoke-virtual {v0}, Landroid/app/Activity;->isFinishing()Z

    move-result v1

    if-eqz v1, :cond_run

    goto :cond_done

    :cond_run
    invoke-static {}, Lcom/alightcreative/app/motion/scene/visualeffect/GmFxStatus;->isDone()Z

    move-result v1

    invoke-static {}, Lcom/alightcreative/app/motion/scene/visualeffect/GmFxStatus;->getTotal()I

    move-result v2

    invoke-static {}, Lcom/alightcreative/app/motion/scene/visualeffect/GmFxStatus;->getCount()I

    move-result v3

    const/4 v4, 0x0

    if-lez v2, :cond_pct

    const/16 v5, 0x64

    mul-int v4, v3, v5

    div-int v4, v4, v2

    :cond_pct
    if-eqz v1, :cond_cap

    goto :goto_apply

    :cond_cap
    const/16 v5, 0x63

    if-le v4, v5, :goto_apply

    const/16 v4, 0x63

    :goto_apply
    iget-object v5, p0, Lcom/goldmotion/startup/GoldStartupActivity$9;->bar:Landroid/widget/ProgressBar;

    if-eqz v1, :cond_bar

    const/16 v6, 0x64

    goto :goto_bar

    :cond_bar
    move v6, v4

    :goto_bar
    invoke-virtual {v5, v6}, Landroid/widget/ProgressBar;->setProgress(I)V

    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v6, "%"

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    iget-object v6, p0, Lcom/goldmotion/startup/GoldStartupActivity$9;->pct:Landroid/widget/TextView;

    invoke-virtual {v6, v5}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    if-eqz v1, :cond_tick

    goto :cond_finish

    :cond_tick
    iget v5, p0, Lcom/goldmotion/startup/GoldStartupActivity$9;->ticks:I

    const/16 v6, 0x12c

    if-ge v5, v6, :cond_finish

    add-int/lit8 v5, v5, 0x1

    iput v5, p0, Lcom/goldmotion/startup/GoldStartupActivity$9;->ticks:I

    iget-object v5, p0, Lcom/goldmotion/startup/GoldStartupActivity$9;->status:Landroid/widget/TextView;

    const-string v6, "STARTING THE ENGINE\u2026"

    invoke-virtual {v5, v6}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    invoke-static {v0}, Lcom/goldmotion/startup/GoldStartupActivity;->access$1400(Lcom/goldmotion/startup/GoldStartupActivity;)Landroid/os/Handler;

    move-result-object v0

    const-wide/16 v5, 0x64

    invoke-virtual {v0, p0, v5, v6}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    return-void

    :cond_finish
    iget-object v1, p0, Lcom/goldmotion/startup/GoldStartupActivity$9;->status:Landroid/widget/TextView;

    const-string v2, "LET'S COOK, EDITORS"

    invoke-virtual {v1, v2}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    iget-object v1, p0, Lcom/goldmotion/startup/GoldStartupActivity$9;->bar:Landroid/widget/ProgressBar;

    const/16 v2, 0x64

    invoke-virtual {v1, v2}, Landroid/widget/ProgressBar;->setProgress(I)V

    const-string v1, "goldmotion.profile"

    const/4 v2, 0x0

    invoke-virtual {v0, v1, v2}, Lcom/goldmotion/startup/GoldStartupActivity;->getSharedPreferences(Ljava/lang/String;I)Landroid/content/SharedPreferences;

    move-result-object v1

    invoke-interface {v1}, Landroid/content/SharedPreferences;->edit()Landroid/content/SharedPreferences$Editor;

    move-result-object v1

    const-string v2, "onboarding_complete"

    const/4 v3, 0x1

    invoke-interface {v1, v2, v3}, Landroid/content/SharedPreferences$Editor;->putBoolean(Ljava/lang/String;Z)Landroid/content/SharedPreferences$Editor;

    move-result-object v1

    invoke-interface {v1}, Landroid/content/SharedPreferences$Editor;->apply()V

    new-instance v1, Lcom/goldmotion/startup/GmLaunchRetry;

    invoke-direct {v1, v0}, Lcom/goldmotion/startup/GmLaunchRetry;-><init>(Lcom/goldmotion/startup/GoldStartupActivity;)V

    invoke-static {v0}, Lcom/goldmotion/startup/GoldStartupActivity;->access$1400(Lcom/goldmotion/startup/GoldStartupActivity;)Landroid/os/Handler;

    move-result-object v0

    const-wide/16 v2, 0x2bc

    invoke-virtual {v0, v1, v2, v3}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    :cond_done
    return-void
.end method
