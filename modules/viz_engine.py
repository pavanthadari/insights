import matplotlib.pyplot as plt
import io, base64

def generate_visuals(df):
    # Example: histogram of first numeric column
    col = df.select_dtypes(include='number').columns[0]
    plt.figure()
    df[col].hist()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_str = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    return [f"data:image/png;base64,{img_str}"]