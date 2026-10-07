# Sound Lab

A private, local browser app for learning sample rate and sample resolution (bit depth).

## Start on this Mac

Double-click **Start Sound Lab.command**. Keep its Terminal window open while using the app. It opens your default browser on a local address. Press Control-C in that Terminal window when finished.

The launcher uses Python 3, which is installed on this Mac. No package installation or account is needed. On another computer with Python 3, run `python3 launcher.py` from this folder. You can also open index.html directly for upload and demo playback; microphone support from a file address varies by browser, so use the launcher for recording.

## Try it

1. Press Play to hear the included melody and high-frequency sweep.
2. While it plays, move Sample rate from 44,100 Hz to 8,000 Hz. Listen for less high-frequency detail.
3. Restore the sample rate, then reduce Sample resolution from 16 bits to 4 bits. Listen for quantization distortion as notes fade.
4. Switch between Original and Adjusted sound to compare at the same position.
5. Upload audio, or click Record microphone, allow browser access, speak, and click Stop recording. Then press Play.
6. Download adjusted WAV to keep the result.

## What the controls mean

- Sample rate: samples per second. A 12th-order Butterworth low-pass filter at 45% of the target rate removes high frequencies before downsampling. Audio is then resampled at the selected rate using the browser's offline audio renderer. The filter has a transition band, so attenuation begins below the ideal Nyquist limit. Pitch and duration stay the same; reducing the rate restricts the frequencies the signal can represent.
- Sample resolution / bit depth: amplitude precision. A signed uniform PCM quantizer uses 2^bits possible levels. No dither is added, making quantization distortion easier to hear.
- The waveform shows 6 milliseconds. Gray is original working audio; orange dots are adjusted samples. Connecting lines help show the points and are not the exact analog reconstruction waveform.
- “Original” means decoded audio mixed to mono. The working sample rate is not necessarily the source file's original rate: the browser may resample during decoding. Increasing a setting cannot restore detail already missing in your recording or file.
- Hardware output and microphone capture use the rates supported by the browser/device. The sliders change the processed signal, not the laptop's hardware configuration.
- Ideal PCM rate = selected sample rate × selected bit depth × 1 mono channel. This is educational, not the export's actual byte rate.
- Export uses the selected sample rate and a 16-bit PCM WAV container. For example, a 4-bit setting has 16 effective amplitude levels stored inside a conventional 16-bit file. This keeps exports widely playable.

Audio is processed in your browser; it is not sent to a server. Audio is mixed to mono. Recordings stop at 60 seconds; uploaded audio is trimmed to the first 60 seconds. File size is limited to 100 MB. Supported input formats depend on your browser. Refreshing or closing the page discards unsaved audio. Your browser may apply microphone processing even when requested off.

Built with the standard Web Audio API: https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API


## Students are welcome to contribute

This is a learning project for our Computer Science class. You can help improve Sound Lab, even if you are new to coding.

**Project link:** [Sound Lab on GitHub](https://github.com/PineappleKshao/sound-lab)

### Ways to help

- Suggest a new sound experiment or a useful feature.
- Improve an explanation of sample rate or bit depth.
- Report a problem you found while using the app.
- Improve the layout, labels, or keyboard controls.
- Make a small code change and explain how it helps students learn.

### Share an idea or report a problem

Open an [issue](https://github.com/PineappleKshao/sound-lab/issues). Describe your idea, or explain what you did, what you expected, and what actually happened. For a bug, include your browser and the audio settings you used. Try to reproduce it with the built-in demo so other students can try it too.

### Submit a change

1. **Fork** the repository to create your own copy on GitHub.
2. Create a branch in your fork, such as `improve-help-text`.
3. Make one small change. The app's HTML, CSS, and JavaScript are all in `index.html`; explanations are in `README.md`.
4. Test your change. For app changes, check that the demo plays, the sliders work, and Original/Adjusted comparison still works. For README changes, check the Markdown preview.
5. Commit your change and push it to your fork if you worked locally.
6. Open a **pull request** to this repository's `main` branch. Explain what you changed, why, and how you checked it.

A pull request lets the project owner review your work before it becomes part of the shared app. See [GitHub's contribution guide](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project) for help with your first contribution.

Keep feedback kind and specific. If you work as a group, explain each person's contribution. Please do not upload classmates' recordings or personal information to public issues or commits.
