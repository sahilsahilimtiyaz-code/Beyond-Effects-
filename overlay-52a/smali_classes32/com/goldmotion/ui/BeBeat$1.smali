# BE52
.class Lcom/goldmotion/ui/BeBeat$1;
.super Ljava/lang/Object;
.source "BeBeat.java"

# interfaces
.implements Landroid/view/View$OnClickListener;


# instance fields
.field final synthetic val$a:Landroid/app/Activity;


# direct methods
.method constructor <init>(Landroid/app/Activity;)V
    .locals 0

    iput-object p1, p0, Lcom/goldmotion/ui/BeBeat$1;->val$a:Landroid/app/Activity;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onClick(Landroid/view/View;)V
    .locals 1

    :try_start_0
    iget-object p1, p0, Lcom/goldmotion/ui/BeBeat$1;->val$a:Landroid/app/Activity;

    invoke-static {p1}, Lcom/goldmotion/beatmark/BeatMarkController;->openDialog(Landroid/app/Activity;)V
    :try_end_0
    .catch Ljava/lang/Throwable; {:try_start_0 .. :try_end_0} :be_b1_catch

    :be_b1_catch
    return-void
.end method
