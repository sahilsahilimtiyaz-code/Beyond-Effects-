.class Lcom/goldmotion/ui/BeUpdate$Show;
.super Ljava/lang/Object;
.implements Ljava/lang/Runnable;
.source "BeUpdate"

.field private final act:Landroid/app/Activity;

.field private final tag:Ljava/lang/String;

.field private final url:Ljava/lang/String;

.method constructor <init>(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;)V
    .locals 0

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    iput-object p1, p0, Lcom/goldmotion/ui/BeUpdate$Show;->act:Landroid/app/Activity;

    iput-object p2, p0, Lcom/goldmotion/ui/BeUpdate$Show;->tag:Ljava/lang/String;

    iput-object p3, p0, Lcom/goldmotion/ui/BeUpdate$Show;->url:Ljava/lang/String;

    return-void
.end method

.method public run()V
    .locals 4

    :try_start_0
    new-instance v0, Landroid/app/AlertDialog$Builder;

    iget-object v1, p0, Lcom/goldmotion/ui/BeUpdate$Show;->act:Landroid/app/Activity;

    invoke-direct {v0, v1}, Landroid/app/AlertDialog$Builder;-><init>(Landroid/content/Context;)V

    const-string v1, "Update available"

    invoke-virtual {v0, v1}, Landroid/app/AlertDialog$Builder;->setTitle(Ljava/lang/CharSequence;)Landroid/app/AlertDialog$Builder;

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "A new Beyond Effects build is ready: "

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v2, p0, Lcom/goldmotion/ui/BeUpdate$Show;->tag:Ljava/lang/String;

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v2, ". Get it from GitHub? (If the install is refused, uninstall the old build first.)"

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/app/AlertDialog$Builder;->setMessage(Ljava/lang/CharSequence;)Landroid/app/AlertDialog$Builder;

    new-instance v1, Lcom/goldmotion/ui/BeUpdate$Go;

    iget-object v2, p0, Lcom/goldmotion/ui/BeUpdate$Show;->act:Landroid/app/Activity;

    iget-object v3, p0, Lcom/goldmotion/ui/BeUpdate$Show;->url:Ljava/lang/String;

    invoke-direct {v1, v2, v3}, Lcom/goldmotion/ui/BeUpdate$Go;-><init>(Landroid/app/Activity;Ljava/lang/String;)V

    const-string v2, "Download"

    invoke-virtual {v0, v2, v1}, Landroid/app/AlertDialog$Builder;->setPositiveButton(Ljava/lang/CharSequence;Landroid/content/DialogInterface$OnClickListener;)Landroid/app/AlertDialog$Builder;

    const-string v1, "Later"

    const/4 v2, 0x0

    invoke-virtual {v0, v1, v2}, Landroid/app/AlertDialog$Builder;->setNegativeButton(Ljava/lang/CharSequence;Landroid/content/DialogInterface$OnClickListener;)Landroid/app/AlertDialog$Builder;

    invoke-virtual {v0}, Landroid/app/AlertDialog$Builder;->create()Landroid/app/AlertDialog;

    move-result-object v0

    invoke-virtual {v0}, Landroid/app/AlertDialog;->show()V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :be_s_catch

    :be_s_catch
    return-void
.end method
