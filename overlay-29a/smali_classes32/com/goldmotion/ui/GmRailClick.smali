.class public final Lcom/goldmotion/ui/GmRailClick;
.super Ljava/lang/Object;
.source "GmRailClick.java"

# interfaces
.implements Landroid/view/View$OnClickListener;


# instance fields
.field private final opener:Landroid/view/View;

.field private final sheet:Landroid/view/View;

.field private final tab:Landroid/view/View;


# direct methods
.method public constructor <init>(Landroid/view/View;Landroid/view/View;Landroid/view/View;)V
    .locals 0

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    iput-object p1, p0, Lcom/goldmotion/ui/GmRailClick;->opener:Landroid/view/View;

    iput-object p2, p0, Lcom/goldmotion/ui/GmRailClick;->sheet:Landroid/view/View;

    iput-object p3, p0, Lcom/goldmotion/ui/GmRailClick;->tab:Landroid/view/View;

    return-void
.end method


# virtual methods
.method public onClick(Landroid/view/View;)V
    .locals 1

    :try_start_0
    iget-object p1, p0, Lcom/goldmotion/ui/GmRailClick;->sheet:Landroid/view/View;

    if-eqz p1, :cond_open

    invoke-virtual {p1}, Landroid/view/View;->getVisibility()I

    move-result p1

    if-nez p1, :cond_tab

    :cond_open
    iget-object p1, p0, Lcom/goldmotion/ui/GmRailClick;->opener:Landroid/view/View;

    if-eqz p1, :cond_tab

    invoke-virtual {p1}, Landroid/view/View;->performClick()Z

    :cond_tab
    iget-object p1, p0, Lcom/goldmotion/ui/GmRailClick;->tab:Landroid/view/View;

    if-eqz p1, :cond_0

    invoke-virtual {p1}, Landroid/view/View;->performClick()Z

    :cond_0
    return-void
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    :catchall_0
    return-void
.end method
