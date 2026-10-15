.class public final Lcom/goldmotion/ui/GmEditorWiring;
.super Ljava/lang/Object;
.source "GmEditorWiring.java"


# direct methods
.method public constructor <init>()V
    .locals 0

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method private static v(Landroid/app/Activity;Ljava/lang/String;)Landroid/view/View;
    .locals 3

    :try_start_0
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    const-string v1, "id"

    invoke-virtual {p0}, Landroid/app/Activity;->getPackageName()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v0, p1, v1, v2}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I

    move-result p1

    if-nez p1, :cond_0

    const/4 p0, 0x0

    return-object p0

    :cond_0
    invoke-virtual {p0, p1}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object p0

    return-object p0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    :catchall_0
    const/4 p0, 0x0

    return-object p0
.end method

.method private static wire2(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V
    .locals 2

    :try_start_0
    invoke-static {p0, p1}, Lcom/goldmotion/ui/GmEditorWiring;->v(Landroid/app/Activity;Ljava/lang/String;)Landroid/view/View;

    move-result-object p1

    if-nez p1, :cond_0

    return-void

    :cond_0
    invoke-static {p0, p2}, Lcom/goldmotion/ui/GmEditorWiring;->v(Landroid/app/Activity;Ljava/lang/String;)Landroid/view/View;

    move-result-object p2

    if-eqz p3, :cond_s

    invoke-static {p0, p3}, Lcom/goldmotion/ui/GmEditorWiring;->v(Landroid/app/Activity;Ljava/lang/String;)Landroid/view/View;

    move-result-object p0

    goto :cond_w

    :cond_s
    const/4 p0, 0x0

    :cond_w
    if-eqz p2, :cond_1

    new-instance p3, Lcom/goldmotion/ui/GmPerformClick;

    invoke-direct {p3, p2, p0}, Lcom/goldmotion/ui/GmPerformClick;-><init>(Landroid/view/View;Landroid/view/View;)V

    invoke-virtual {p1, p3}, Landroid/view/View;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    :cond_1
    return-void
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    :catchall_0
    return-void
.end method

.method public static wire(Landroid/app/Activity;)V
    .locals 3

    :try_start_0
    const-string v0, "beNavUndo"

    const-string v1, "buttonUndo"

    const/4 v2, 0x0

    invoke-static {p0, v0, v1, v2}, Lcom/goldmotion/ui/GmEditorWiring;->wire2(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V

    const-string v0, "beNavRedo"

    const-string v1, "buttonRedo"

    invoke-static {p0, v0, v1, v2}, Lcom/goldmotion/ui/GmEditorWiring;->wire2(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V

    const-string v0, "beExportPill"

    const-string v1, "share"

    invoke-static {p0, v0, v1, v2}, Lcom/goldmotion/ui/GmEditorWiring;->wire2(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V

    const-string v0, "beRailMedia"

    const-string v1, "tabAddImageVideo"

    invoke-static {p0, v0, v1}, Lcom/goldmotion/ui/GmEditorWiring;->wireRail(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;)V

    const-string v0, "beRailTemplates"

    const-string v1, "tabAddTemplates"

    invoke-static {p0, v0, v1}, Lcom/goldmotion/ui/GmEditorWiring;->wireRail(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;)V

    const-string v0, "beRailAudio"

    const-string v1, "tabAddAudio"

    invoke-static {p0, v0, v1}, Lcom/goldmotion/ui/GmEditorWiring;->wireRail(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;)V

    const-string v0, "beRailText"

    const-string v1, "buttonAddText"

    const/4 v2, 0x0

    invoke-static {p0, v0, v1, v2}, Lcom/goldmotion/ui/GmEditorWiring;->wire2(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V

    const-string v0, "beRailAI"

    invoke-static {p0, v0}, Lcom/goldmotion/ui/GmEditorWiring;->wireTool(Landroid/app/Activity;Ljava/lang/String;)V

    const-string v0, "beRailElements"

    const-string v1, "tabAddObject"

    invoke-static {p0, v0, v1}, Lcom/goldmotion/ui/GmEditorWiring;->wireRail(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;)V

    const-string v0, "beSheetHandle"

    const-string v1, "buttonAdd"

    const/4 v2, 0x0

    invoke-static {p0, v0, v1, v2}, Lcom/goldmotion/ui/GmEditorWiring;->wire2(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V

    return-void
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    :catchall_0
    return-void
.end method

.method private static wireTool(Landroid/app/Activity;Ljava/lang/String;)V
    .locals 2

    :try_start_0
    invoke-static {p0, p1}, Lcom/goldmotion/ui/GmEditorWiring;->v(Landroid/app/Activity;Ljava/lang/String;)Landroid/view/View;

    move-result-object p1

    if-nez p1, :cond_0

    return-void

    :cond_0
    new-instance v0, Lcom/goldmotion/ui/GmToolLauncher;

    const-string v1, "Twixtor"

    invoke-direct {v0, p0, v1}, Lcom/goldmotion/ui/GmToolLauncher;-><init>(Landroid/app/Activity;Ljava/lang/String;)V

    invoke-virtual {p1, v0}, Landroid/view/View;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    return-void
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    :catchall_0
    return-void
.end method

.method private static wireRail(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;)V
    .locals 4

    :try_start_0
    invoke-static {p0, p1}, Lcom/goldmotion/ui/GmEditorWiring;->v(Landroid/app/Activity;Ljava/lang/String;)Landroid/view/View;

    move-result-object p1

    if-nez p1, :cond_0

    return-void

    :cond_0
    invoke-static {p0, p2}, Lcom/goldmotion/ui/GmEditorWiring;->v(Landroid/app/Activity;Ljava/lang/String;)Landroid/view/View;

    move-result-object p2

    if-nez p2, :cond_1

    return-void

    :cond_1
    const-string v0, "buttonAdd"

    invoke-static {p0, v0}, Lcom/goldmotion/ui/GmEditorWiring;->v(Landroid/app/Activity;Ljava/lang/String;)Landroid/view/View;

    move-result-object v0

    const-string v1, "addPopup"

    invoke-static {p0, v1}, Lcom/goldmotion/ui/GmEditorWiring;->v(Landroid/app/Activity;Ljava/lang/String;)Landroid/view/View;

    move-result-object p0

    new-instance v1, Lcom/goldmotion/ui/GmRailClick;

    invoke-direct {v1, v0, p0, p2}, Lcom/goldmotion/ui/GmRailClick;-><init>(Landroid/view/View;Landroid/view/View;Landroid/view/View;)V

    invoke-virtual {p1, v1}, Landroid/view/View;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    return-void
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    :catchall_0
    return-void
.end method
