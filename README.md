> Dataset sources: COMMONS NORMAL KNEE X-ray

---

### 02 - `OpenCV X-ray | 02-xray-opencv/`
**Goal:** Classic medical image preprocessing pipeline.

**Pipeline:**
1. Read chest X-ray
2. Convert to grayscale
3. Gaussian blur (5x5) to reduce noise
4. Canny edge detection (50, 150 thresholds)
5. Plot Original | Grayscale | Edges side-by-side
   
**Result:**
- `Knee_X-ray.png` - Original vs Grayscale vs Canny Edges

**Run:**
```bash
pip install opencv-python matplotlib
python xray_edges.py
