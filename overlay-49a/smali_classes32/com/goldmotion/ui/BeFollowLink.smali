.class public final Lcom/goldmotion/ui/BeFollowLink;
.super Ljava/lang/Object;
.implements Landroid/view/View$OnClickListener;
.source "BeFollowLink"


# instance fields
.field private final act:Landroid/app/Activity;

.field private final url:Ljava/lang/String;


# direct methods
.method public constructor <init>(Landroid/app/Activity;Ljava/lang/String;)V
    .locals 0

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    iput-object p1, p0, Lcom/goldmotion/ui/BeFollowLink;->act:Landroid/app/Activity;

    iput-object p2, p0, Lcom/goldmotion/ui/BeFollowLink;->url:Ljava/lang/String;

    return-void
.end method


# virtual methods
.method public onClick(Landroid/view/View;)V
    .locals 3

    :try_start_0
    iget-object v0, p0, Lcom/goldmotion/ui/BeFollowLink;->act:Landroid/app/Activity;

    invoke-static {v0}, Lcom/goldmotion/ui/BeFollow;->mark(Landroid/content/Context;)V

    invoke-static {v0}, Lcom/goldmotion/ui/BeNotify;->hideDot(Landroid/app/Activity;)V

    new-instance v1, Landroid/content/Intent;

    const-string v2, "android.intent.action.VIEW"

    invoke-direct {v1, v2}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    iget-object v2, p0, Lcom/goldmotion/ui/BeFollowLink;->url:Ljava/lang/String;

    invoke-static {v2}, Landroid/net/Uri;->parse(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v2

    invoke-virtual {v1, v2}, Landroid/content/Intent;->setData(Landroid/net/Uri;)Landroid/content/Intent;

    invoke-virtual {v0, v1}, Landroid/app/Activity;->startActivity(Landroid/content/Intent;)V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    return-void

    :catch_0
    move-exception v0

    return-void
.end method
