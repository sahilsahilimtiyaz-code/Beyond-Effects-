.class public final Lcom/goldmotion/ui/GmToolLauncher;
.super Ljava/lang/Object;
.source "GmToolLauncher.java"

# interfaces
.implements Landroid/view/View$OnClickListener;


# instance fields
.field private final act:Landroid/app/Activity;

.field private final tool:Ljava/lang/String;


# direct methods
.method public constructor <init>(Landroid/app/Activity;Ljava/lang/String;)V
    .locals 0

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    iput-object p1, p0, Lcom/goldmotion/ui/GmToolLauncher;->act:Landroid/app/Activity;

    iput-object p2, p0, Lcom/goldmotion/ui/GmToolLauncher;->tool:Ljava/lang/String;

    return-void
.end method


# virtual methods
.method public onClick(Landroid/view/View;)V
    .locals 3

    :try_start_0
    iget-object p1, p0, Lcom/goldmotion/ui/GmToolLauncher;->act:Landroid/app/Activity;

    if-eqz p1, :cond_0

    new-instance v0, Landroid/content/Intent;

    const-class v1, Lcom/goldmotion/tools/ToolStudioActivity;

    invoke-direct {v0, p1, v1}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    iget-object v1, p0, Lcom/goldmotion/ui/GmToolLauncher;->tool:Ljava/lang/String;

    if-eqz v1, :cond_1

    const-string v2, "gold_tool"

    invoke-virtual {v0, v2, v1}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    :cond_1
    invoke-virtual {p1, v0}, Landroid/app/Activity;->startActivity(Landroid/content/Intent;)V

    :cond_0
    return-void
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    :catchall_0
    return-void
.end method
