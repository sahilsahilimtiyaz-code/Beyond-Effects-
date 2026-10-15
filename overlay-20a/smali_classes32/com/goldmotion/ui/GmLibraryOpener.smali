.class public final Lcom/goldmotion/ui/GmLibraryOpener;
.super Ljava/lang/Object;
.source "GmLibraryOpener.java"

# interfaces
.implements Landroid/view/View$OnClickListener;


# instance fields
.field private final act:Landroid/app/Activity;


# direct methods
.method public constructor <init>(Landroid/app/Activity;)V
    .locals 0

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    iput-object p1, p0, Lcom/goldmotion/ui/GmLibraryOpener;->act:Landroid/app/Activity;

    return-void
.end method


# virtual methods
.method public onClick(Landroid/view/View;)V
    .locals 2

    iget-object p1, p0, Lcom/goldmotion/ui/GmLibraryOpener;->act:Landroid/app/Activity;

    const/4 v0, 0x1

    invoke-static {p1, v0}, Lcom/goldmotion/navbar/GmNavBar;->pick(Landroid/app/Activity;I)V

    return-void
.end method
