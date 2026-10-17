.class Lcom/goldmotion/ui/BeUpdate$Go;
.super Ljava/lang/Object;
.implements Landroid/content/DialogInterface$OnClickListener;
.source "BeUpdate"

.field private final act:Landroid/app/Activity;

.field private final url:Ljava/lang/String;

.method constructor <init>(Landroid/app/Activity;Ljava/lang/String;)V
    .locals 0

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    iput-object p1, p0, Lcom/goldmotion/ui/BeUpdate$Go;->act:Landroid/app/Activity;

    iput-object p2, p0, Lcom/goldmotion/ui/BeUpdate$Go;->url:Ljava/lang/String;

    return-void
.end method

.method public onClick(Landroid/content/DialogInterface;I)V
    .locals 3

    :try_start_0
    new-instance v0, Landroid/content/Intent;

    const-string v1, "android.intent.action.VIEW"

    invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    iget-object v1, p0, Lcom/goldmotion/ui/BeUpdate$Go;->url:Ljava/lang/String;

    invoke-static {v1}, Landroid/net/Uri;->parse(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/content/Intent;->setData(Landroid/net/Uri;)Landroid/content/Intent;

    iget-object v1, p0, Lcom/goldmotion/ui/BeUpdate$Go;->act:Landroid/app/Activity;

    invoke-virtual {v1, v0}, Landroid/app/Activity;->startActivity(Landroid/content/Intent;)V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :be_g_catch

    :be_g_catch
    return-void
.end method
