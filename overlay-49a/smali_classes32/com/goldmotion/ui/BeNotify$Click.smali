.class public final Lcom/goldmotion/ui/BeNotify$Click;
.super Ljava/lang/Object;
.implements Landroid/view/View$OnClickListener;
.source "BeNotify"


# instance fields
.field private final act:Landroid/app/Activity;


# direct methods
.method public constructor <init>(Landroid/app/Activity;)V
    .locals 0

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    iput-object p1, p0, Lcom/goldmotion/ui/BeNotify$Click;->act:Landroid/app/Activity;

    return-void
.end method


# virtual methods
.method public onClick(Landroid/view/View;)V
    .locals 1

    iget-object v0, p0, Lcom/goldmotion/ui/BeNotify$Click;->act:Landroid/app/Activity;

    invoke-static {v0}, Lcom/goldmotion/ui/BeNotify;->show(Landroid/app/Activity;)V

    return-void
.end method
