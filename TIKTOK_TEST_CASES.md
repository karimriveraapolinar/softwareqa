# Test Cases

## TC_VIDLEN_HIGH1
**Title:** Verify if video length is too high

**Preconditions:**
- User account exists
- User is logged in
- User has created a video

**Test Type:** Edge Case

**Steps:**
1. User clicks create/upload button
2. User selects a video 20 minutes long
3. User attempts to upload video

**Test Data:**
- File: test_video.mp4
- Format: MP4
- Size: 67MB
- Length: 20 Minutes
- Resolution: 1080x1920
- Aspect Ratio: 9:16
- Caption: "Test upload"

**Expected:**
- A popup is displayed on the users device stating videos longer than 10 minutes are not allowed
- Upload is unsuccessful
- User is urged to attempt another upload with a shorter video

**Priority:** Low

---

## TC_VIDLEN_LOW1
**Title:** Verify if video length is too low

**Preconditions:**
- User account exists
- User is logged in
- User has created a video

**Test Type:** Edge Case

**Steps:**
1. User clicks create/upload button
2. User selects a video 1 seconds long
3. User attempts to upload video

**Test Data:**
- File: test_video.mp4
- Format: MP4
- Size: 67MB
- Length: 1 seconds
- Resolution: 1080x1920
- Aspect Ratio: 9:16
- Caption: "Test upload"

**Expected:**
- A popup is displayed on the users device stating videos shorter than 3 seconds are not allowed
- Upload is unsuccessful
- User is urged to attempt another upload with a longer video

**Priority:** Low

---

## TC_VIDLEN_HIGH2
**Title:** Verify if video length is too high

**Preconditions:**
- User account exists
- User is logged in
- User has created a video

**Test Type:** Boundary

**Steps:**
1. User clicks create/upload button
2. User selects a video 10 minutes 1 second long
3. User attempts to upload video

**Test Data:**
- File: test_video.mp4
- Format: MP4
- Size: 67MB
- Length: 10 Minutes 1 Second
- Resolution: 1080x1920
- Aspect Ratio: 9:16
- Caption: "Test upload"

**Expected:**
- A popup is displayed on the users device stating videos longer than 10 minutes are not allowed
- Upload is unsuccessful
- User is urged to attempt another upload with a shorter video

**Priority:** Low

---

## TC_VIDLEN_LOW2
**Title:** Verify if video length is too low

**Preconditions:**
- User account exists
- User is logged in
- User has created a video

**Test Type:** Boundary

**Steps:**
1. User clicks create/upload button
2. User selects a video 2 seconds long
3. User attempts to upload video

**Test Data:**
- File: test_video.mp4
- Format: MP4
- Size: 67MB
- Length: 2 seconds
- Resolution: 1080x1920
- Aspect Ratio: 9:16
- Caption: "Test upload"

**Expected:**
- A popup is displayed on the users device stating videos shorter than 3 seconds are not allowed
- Upload is unsuccessful
- User is urged to attempt another upload with a longer video

**Priority:** Low

---

## TC_VIDUPLOAD_1
**Title:** Verify that AVI formatted files upload seamlessly

**Preconditions:**
- User account exists
- User is logged in
- User has created an AVI formatted video

**Test Type:** Positive

**Steps:**
1. User clicks create/upload button
2. User selects a AVI formatted video
3. User attempts to upload video

**Test Data:**
- File: test_video.AVI
- Format: AVI
- Size: 67MB
- Length: 45 seconds
- Resolution: 1080x1920
- Aspect Ratio: 9:16
- Caption: "Test upload"

**Expected:**
- Upload is successful

**Priority:** High

---

## TC_VIDUPLOAD_2
**Title:** Verify that videos with a size of 256 upload seamlessly

**Preconditions:**
- User account exists
- User is logged in
- User has created a video with a file size of 256MB

**Test Type:** Positive

**Steps:**
1. User clicks create/upload button
2. User selects a video with a size of 256MB
3. User attempts to upload video

**Test Data:**
- File: test_video.mp4
- Format: MP4
- Size: 256MB
- Length: 45 seconds
- Resolution: 1080x1920
- Aspect Ratio: 9:16
- Caption: "Test upload"

**Expected:**
- Upload is successful

**Priority:** High

---

## TC_FORMAT_NEG1
**Title:** Verify if the video is on the supported format

**Test Type:** Negative

**Preconditions:**
- User account exists
- User is on login page
- User created a video

**Steps:**
1. User is logged in
2. Create a video with MKV
3. Click post

**Test Data:**
- File: test_video.mkv
- Format: MKV
- Size: 67MB
- Length: 9
- Resolution: 1080x1920
- Aspect Ratio: 9:16
- Caption: "Test upload"

**Expected:**
- User gets a warning popup
- Warning message says video is recorded in the wrong format and tells the user to change it to mp4
- Returns back to the editing

**Priority:** High

---

## TC_ASPECT_NEG2
**Title:** Verify if the video's aspect ratio stays within the 9:16 range

**Test Type:** Negative

**Preconditions:**
- User account exists
- User is on login page
- User created a video

**Steps:**
1. User is logged in
2. Create a video in horizontal view
3. Click post

**Test Data:**
- File: test_video.mp4
- Format: MP4
- Size: 67MB
- Length: 9
- Resolution: 1080x1920
- Aspect Ratio: 12:16
- Caption: "Test upload"

**Expected:**
- User gets a warning popup
- Warning message says video's aspect ratio is messed up
- Returns back to the editing

**Priority:** Medium

---

## TC_PUBLISHBUTT
**Title:** Verify that the publish button works

**Preconditions:**
- User account exists
- User is logged in
- User has a video to upload

**Test Type:** Black Box

**Steps:**
1. User clicks create/upload button
2. User selects a video
3. User attempts to upload video

**Test Data:**
- File: test_video.mp4
- Format: MP4
- Size: 256MB
- Length: 45 seconds
- Resolution: 1080x1920
- Aspect Ratio: 9:16
- Caption: "Test upload"

**Expected:**
- Upload is successful

**Priority:** High

---

## TC_PUBLIC10
**Title:** Verify that the video the user posted is public

**Preconditions:**
- User account exists
- User is logged in
- User has created a video with a file size of 256MB
- User has posted a public video

**Test Type:** Black Box

**Steps:**
1. User clicks create/upload button
2. User selects a video with a size of 256MB
3. User selects public for video choice
4. User attempts to upload video

**Test Data:**
- File: test_video.mp4
- Format: MP4
- Size: 256MB
- Length: 45 seconds
- Resolution: 1080x1920
- Aspect Ratio: 9:16
- Caption: "Test upload"

**Expected:**
- Upload is successful
- Any user is able to open up TikTok and see the video even if they are not following

**Priority:** High