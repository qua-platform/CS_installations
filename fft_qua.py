# %% 
import numpy as np

def analyze_npz(path):
    print("\n\n\n==============================")
    print(f"=== {os.path.basename(path)} (.npz) 파일 상세 분석 ===")
    print("==============================")
    data = np.load(path)
    
    print("\n📦 저장된 배열 목록:")
    for name in data.files:
        arr = data[name]
        print(f"\nArray Name: {name}")
        print(f"  - Shape: {arr.shape}")
        print(f"  - Dtype: {arr.dtype}")
        # 1차원 이상 배열에 대해서만 샘플 출력
        flat = arr.flatten()
        print(f"  - Sample values (first 5): {flat[:5]}")
        # 2차원 이하 배열이면 통계값 출력
        if arr.ndim <= 2 and flat.size > 0:
            print(f"  - Min: {flat.min():.6f}, Max: {flat.max():.6f}, Mean: {flat.mean():.6f}")

def analyze_file(path):
    ext = os.path.splitext(path)[1].lower()
    if ext in ('.h5', '.hdf5'):
        analyze_h5(path)
    elif ext == '.npz':
        analyze_npz(path)
    else:
        print(f"Unsupported file extension: {ext}")

analyze_file('arrays.npz')
