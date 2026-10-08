# Sound Lab · 聲音實驗室

Explore how computers represent sound. 改變採樣率與位元深度，聽見數位聲音的變化。

<a id="languages"></a>

**[English](#english) · [繁體中文](#traditional-chinese)**

---

<a id="english"></a>

## English

A private, local browser app for learning sample rate and sample resolution (bit depth).

### Start on this Mac

Double-click **Start Sound Lab.command**. Keep its Terminal window open while using the app. It opens your default browser on a local address. Press Control-C in that Terminal window when finished.

The launcher uses Python 3, which is installed on this Mac. No package installation or account is needed. On another computer with Python 3, run `python3 launcher.py` from this folder. You can also open index.html directly for upload and demo playback; microphone support from a file address varies by browser, so use the launcher for recording.

### Try it

1. Press Play to hear the included melody and high-frequency sweep.
2. While it plays, move Sample rate from 44,100 Hz to 8,000 Hz. Listen for less high-frequency detail.
3. Restore the sample rate, then reduce Sample resolution from 16 bits to 4 bits. Listen for quantization distortion as notes fade.
4. Switch between Original and Adjusted sound to compare at the same position.
5. Upload audio, or click Record microphone, allow browser access, speak, and click Stop recording. Then press Play.
6. Download adjusted WAV to keep the result.

### What the controls mean

- Sample rate: samples per second. A 12th-order Butterworth low-pass filter at 45% of the target rate removes high frequencies before downsampling. Audio is then resampled at the selected rate using the browser's offline audio renderer. The filter has a transition band, so attenuation begins below the ideal Nyquist limit. Pitch and duration stay the same; reducing the rate restricts the frequencies the signal can represent.
- Sample resolution / bit depth: amplitude precision. A signed uniform PCM quantizer uses 2^bits possible levels. No dither is added, making quantization distortion easier to hear.
- The waveform shows 6 milliseconds. Gray is original working audio; orange dots are adjusted samples. Connecting lines help show the points and are not the exact analog reconstruction waveform.
- “Original” means decoded audio mixed to mono. The working sample rate is not necessarily the source file's original rate: the browser may resample during decoding. Increasing a setting cannot restore detail already missing in your recording or file.
- Hardware output and microphone capture use the rates supported by the browser/device. The sliders change the processed signal, not the laptop's hardware configuration.
- Ideal PCM rate = selected sample rate × selected bit depth × 1 mono channel. This is educational, not the export's actual byte rate.
- Export uses the selected sample rate and a 16-bit PCM WAV container. For example, a 4-bit setting has 16 effective amplitude levels stored inside a conventional 16-bit file. This keeps exports widely playable.

Audio is processed in your browser; it is not sent to a server. Audio is mixed to mono. Recordings stop at 60 seconds; uploaded audio is trimmed to the first 60 seconds. File size is limited to 100 MB. Supported input formats depend on your browser. Refreshing or closing the page discards unsaved audio. Your browser may apply microphone processing even when requested off.

Built with the standard [Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API).


### Students are welcome to contribute

This is a learning project for our Computer Science class. You can help improve Sound Lab, even if you are new to coding.

**Project link:** [Sound Lab on GitHub](https://github.com/PineappleKshao/sound-lab)

#### Ways to help

- Suggest a new sound experiment or a useful feature.
- Improve an explanation of sample rate or bit depth.
- Report a problem you found while using the app.
- Improve the layout, labels, or keyboard controls.
- Make a small code change and explain how it helps students learn.

#### Share an idea or report a problem

Open an [issue](https://github.com/PineappleKshao/sound-lab/issues). Describe your idea, or explain what you did, what you expected, and what actually happened. For a bug, include your browser and the audio settings you used. Try to reproduce it with the built-in demo so other students can try it too.

#### Submit a change

1. **Fork** the repository to create your own copy on GitHub.
2. Create a branch in your fork, such as `improve-help-text`.
3. Make one small change. The app's HTML, CSS, and JavaScript are all in `index.html`; explanations are in `README.md`.
4. Test your change. For app changes, check that the demo plays, the sliders work, and Original/Adjusted comparison still works. For README changes, check the Markdown preview.
5. Commit your change and push it to your fork if you worked locally.
6. Open a **pull request** to this repository's `main` branch. Explain what you changed, why, and how you checked it.

A pull request lets the project owner review your work before it becomes part of the shared app. See [GitHub's contribution guide](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project) for help with your first contribution.

Keep feedback kind and specific. If you work as a group, explain each person's contribution. Please do not upload classmates' recordings or personal information to public issues or commits.

[Back to language selection / 返回語言選擇](#languages)

---

<a id="traditional-chinese"></a>

## 繁體中文

一個在本機瀏覽器中執行的聲音學習工具，幫助你理解**採樣率**和**採樣解析度（位元深度）**。音訊在瀏覽器中處理，保護你的隱私。

### 在這台 Mac 上啟動

按兩下 **Start Sound Lab.command**。使用時請保持啟動器開啟的「終端機」視窗處於執行狀態。它會在預設瀏覽器中開啟一個本機網址。使用結束後，在該終端機視窗中按 **Control-C** 停止服務。

啟動器使用 Python 3，這台 Mac 已安裝該環境，無需額外安裝套件或註冊帳號。在其他已安裝 Python 3 的電腦上，可以在此資料夾中執行 `python3 launcher.py`。你也可以直接開啟 `index.html` 來上傳音訊和播放示範；但不同瀏覽器對本機檔案頁面的麥克風支援有所不同，因此錄音時建議使用啟動器。

### 動手試一試

1. 點選 **Play（播放）**，聆聽內建旋律和高頻掃頻聲音。
2. 播放時，將 **Sample rate（採樣率）**從 44,100 Hz 調至 8,000 Hz，留意高頻細節的減少。
3. 恢復採樣率，再將 **Sample resolution（採樣解析度）**從 16 位元調至 4 位元，留意音符逐漸變弱時出現的量化失真。
4. 在 **Original（原始）**與 **Adjusted（調整後）**之間切換，在相同播放位置比較聲音。
5. 上傳音訊，或點選 **Record microphone（麥克風錄音）**，允許瀏覽器使用麥克風後說話，再點選 **Stop recording（停止錄音）**，然後播放。
6. 點選 **Download adjusted WAV（下載調整後的 WAV）**儲存結果。

### 控制項與顯示的含義

- **採樣率（Sample rate）**：每秒採集的樣本數。降低採樣率前，程式會使用截止頻率為目標採樣率 45% 的 12 階巴特沃斯低通濾波器，濾除高頻成分，再透過瀏覽器的離線音訊渲染器按所選採樣率重新採樣。濾波器具有過渡帶，因此衰減會在理想的奈奎斯特頻率以下開始。音高和時長保持不變；降低採樣率會限制訊號能夠表示的頻率範圍。
- **採樣解析度／位元深度（Sample resolution / bit depth）**：表示聲音振幅的精細程度。有符號均勻 PCM 量化器使用 `2^位元深度` 個可能的量化級別。程式不添加抖動雜訊（dither），方便你聽出量化失真。
- **波形圖**：顯示 6 毫秒的聲音。灰色表示用於處理的原始音訊，橙色圓點表示調整後的採樣點。連接線幫助你觀察這些點，並不代表精確重建的類比波形。
- **「原始」音訊（Original）**：指解碼後混合為單聲道的音訊。處理時的採樣率不一定等於來源檔案的採樣率，因為瀏覽器可能在解碼時進行重新採樣。提高設定無法恢復錄音或檔案中已經缺失的細節。
- **硬體與處理**：聲音輸出和麥克風錄音使用瀏覽器及裝置支援的採樣率。滑桿改變的是處理後的訊號，而不是筆記型電腦的硬體設定。
- **理想 PCM 位元率**：所選採樣率 × 所選位元深度 × 1 個單聲道。此數值用於學習，並不代表匯出檔案實際每秒佔用的位元組數。
- **匯出格式**：使用所選採樣率，儲存為 16 位元 PCM WAV 檔案。例如，選擇 4 位元時，聲音只有 16 個有效振幅級別，但仍儲存在標準的 16 位元檔案中，以便在更多播放器中播放。

音訊只在你的瀏覽器中處理，不會傳送到伺服器。所有音訊都會混合為單聲道。錄音在 60 秒時自動停止；上傳的音訊只保留前 60 秒，檔案大小上限為 100 MB。可匯入的格式取決於瀏覽器。重新整理或關閉頁面會遺失尚未儲存的音訊。即使程式要求關閉麥克風音訊處理，瀏覽器仍可能套用相關處理。

本專案使用標準的 [Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API) 建構。

### 歡迎同學參與貢獻

這是我們電腦科學課堂的學習專案。即使你剛開始學習程式設計，也可以幫助改進 Sound Lab。

**專案連結：**[GitHub 上的 Sound Lab](https://github.com/PineappleKshao/sound-lab)

#### 你可以做什麼

- 提議新的聲音實驗或實用功能。
- 改進採樣率或位元深度的說明，讓它們更容易理解。
- 回報使用過程中發現的問題。
- 改進頁面版面配置、標籤或鍵盤操作。
- 做一個小的程式碼修改，並說明它如何幫助同學學習。

#### 分享想法或回報問題

提交一個 [Issue（問題或建議）](https://github.com/PineappleKshao/sound-lab/issues)。描述你的想法，或說明你的操作步驟、預期結果和實際結果。如果回報程式錯誤，請註明瀏覽器和所使用的音訊設定。盡量使用內建示範重現問題，方便其他同學一起檢查。

#### 提交修改

1. **Fork（建立個人副本）**：在 GitHub 上建立自己的儲存庫副本。
2. 在自己的副本中建立一個分支，例如 `improve-help-text`。
3. 每次做一個小修改。應用程式的 HTML、CSS 和 JavaScript 都在 `index.html` 中，專案說明在 `README.md` 中。
4. 檢查修改。如果修改應用程式，請確認示範可以播放、滑桿可以使用，且 Original / Adjusted 對比仍然正常。如果修改 README，請檢查 Markdown 預覽。
5. 如果在本機修改，請提交（commit）並推送（push）到自己的儲存庫副本。
6. 向本儲存庫的 `main` 分支發起 **Pull Request（合併請求）**，說明修改內容、修改原因，以及如何檢查結果。

合併請求讓專案負責人能夠在修改納入共用應用程式之前進行審核。第一次貢獻時，可以參考 [GitHub 貢獻指南](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project)。

請友善、具體地提出回饋。小組合作時，請說明每位成員的貢獻。請勿將同學的錄音或個人資訊上傳到公開的 Issue 或程式碼提交中。

[English ↑](#english)
