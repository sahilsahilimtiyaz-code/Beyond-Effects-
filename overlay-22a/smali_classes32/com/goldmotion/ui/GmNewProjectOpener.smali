.class public final Lcom/goldmotion/ui/GmNewProjectOpener;
.super Ljava/lang/Object;
.source "GmNewProjectOpener.java"

# interfaces
.implements Landroid/view/View$OnClickListener;


# instance fields
.field private final act:Landroid/app/Activity;


# direct methods
.method public constructor <init>(Landroid/app/Activity;)V
    .locals 0

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    iput-object p1, p0, Lcom/goldmotion/ui/GmNewProjectOpener;->act:Landroid/app/Activity;

    return-void
.end method


# virtual methods
.method public onClick(Landroid/view/View;)V
    .locals 1

    iget-object p1, p0, Lcom/goldmotion/ui/GmNewProjectOpener;->act:Landroid/app/Activity;

    invoke-static {p1}, Lcom/goldmotion/navbar/GmNavBar;->plus(Landroid/app/Activity;)V

    return-void
.end method
