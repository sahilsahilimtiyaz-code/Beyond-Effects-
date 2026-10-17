.class public final Lcom/goldmotion/ui/BeNotify$Follow;
.super Ljava/lang/Object;
.implements Landroid/view/View$OnClickListener;
.source "BeNotify"


# instance fields
.field private final act:Landroid/app/Activity;

.field private final dlg:Landroid/app/AlertDialog;


# direct methods
.method public constructor <init>(Landroid/app/Activity;Landroid/app/AlertDialog;)V
    .locals 0

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    iput-object p1, p0, Lcom/goldmotion/ui/BeNotify$Follow;->act:Landroid/app/Activity;

    iput-object p2, p0, Lcom/goldmotion/ui/BeNotify$Follow;->dlg:Landroid/app/AlertDialog;

    return-void
.end method


# virtual methods
.method public onClick(Landroid/view/View;)V
    .locals 2

    :try_start_0
    iget-object v0, p0, Lcom/goldmotion/ui/BeNotify$Follow;->act:Landroid/app/Activity;

    invoke-static {v0}, Lcom/goldmotion/ui/BeFollow;->mark(Landroid/content/Context;)V

    invoke-static {v0}, Lcom/goldmotion/ui/BeNotify;->hideDot(Landroid/app/Activity;)V

    invoke-static {v0}, Lcom/goldmotion/ui/BeNotify;->openInstagram(Landroid/app/Activity;)V

    iget-object v1, p0, Lcom/goldmotion/ui/BeNotify$Follow;->dlg:Landroid/app/AlertDialog;

    if-eqz v1, :cond_done

    invoke-virtual {v1}, Landroid/app/AlertDialog;->dismiss()V

    :cond_done
    return-void
    :try_end_0
    .catch Ljava/lang/Throwable; {:try_start_0 .. :try_end_0} :catch_0

    :catch_0
    move-exception v0

    return-void
.end method
