.class Lcom/goldmotion/ui/BeUpdate$Fetch;
.super Ljava/lang/Object;
.implements Ljava/lang/Runnable;
.source "BeUpdate"

.field private final act:Landroid/app/Activity;

.method constructor <init>(Landroid/app/Activity;)V
    .locals 0

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    iput-object p1, p0, Lcom/goldmotion/ui/BeUpdate$Fetch;->act:Landroid/app/Activity;

    return-void
.end method

.method public run()V
    .locals 6

    :try_start_0
    new-instance v0, Ljava/net/URL;

    const-string v1, "https://github.com/sahilsahilimtiyaz-code/Beyond-Effects-/releases/latest"

    invoke-direct {v0, v1}, Ljava/net/URL;-><init>(Ljava/lang/String;)V

    invoke-virtual {v0}, Ljava/net/URL;->openConnection()Ljava/net/URLConnection;

    move-result-object v0

    check-cast v0, Ljava/net/HttpURLConnection;

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Ljava/net/HttpURLConnection;->setInstanceFollowRedirects(Z)V

    const/16 v1, 0x1388

    invoke-virtual {v0, v1}, Ljava/net/HttpURLConnection;->setConnectTimeout(I)V

    invoke-virtual {v0, v1}, Ljava/net/HttpURLConnection;->setReadTimeout(I)V

    const-string v1, "User-Agent"

    const-string v2, "BeyondEffects-Updater"

    invoke-virtual {v0, v1, v2}, Ljava/net/HttpURLConnection;->setRequestProperty(Ljava/lang/String;Ljava/lang/String;)V

    invoke-virtual {v0}, Ljava/net/HttpURLConnection;->getResponseCode()I

    const-string v1, "Location"

    invoke-virtual {v0, v1}, Ljava/net/HttpURLConnection;->getHeaderField(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0}, Ljava/net/HttpURLConnection;->disconnect()V

    if-nez v1, :be_f_end

    const-string v2, "/releases/tag/"

    invoke-virtual {v1, v2}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z

    move-result v2

    if-nez v2, :be_f_end

    const/16 v2, 0x2f

    invoke-virtual {v1, v2}, Ljava/lang/String;->lastIndexOf(I)I

    move-result v2

    add-int/lit8 v2, v2, 0x1

    invoke-virtual {v1, v2}, Ljava/lang/String;->substring(I)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/String;->length()I

    move-result v3

    if-eqz v3, :be_f_end

    sget-object v3, Lcom/goldmotion/ui/BeUpdate;->BE_BUILD_TAG:Ljava/lang/String;

    invoke-virtual {v3, v2}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v3

    if-nez v3, :be_f_end

    iget-object v3, p0, Lcom/goldmotion/ui/BeUpdate$Fetch;->act:Landroid/app/Activity;

    new-instance v4, Lcom/goldmotion/ui/BeUpdate$Show;

    invoke-direct {v4, v3, v2, v1}, Lcom/goldmotion/ui/BeUpdate$Show;-><init>(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;)V

    invoke-virtual {v3, v4}, Landroid/app/Activity;->runOnUiThread(Ljava/lang/Runnable;)V

    :be_f_end
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :be_f_catch

    :be_f_catch
    return-void
.end method
