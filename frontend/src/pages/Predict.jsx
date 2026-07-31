import { useState } from "react";
import api from "../api/api";

function Predict() {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);

  const [loading, setLoading] = useState(false);

  const [result, setResult] = useState(null);

  const handleImage = (e) => {
    const file = e.target.files[0];

    if (!file) return;

    setImage(file);
    setPreview(URL.createObjectURL(file));
  };

  const handlePredict = async () => {
    if (!image) {
      alert("Please select an image.");
      return;
    }

    const formData = new FormData();
    formData.append("file", image);

    try {
      setLoading(true);

      const response = await api.post("/predict", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Prediction failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-5xl mx-auto p-8">

      <h1 className="text-4xl font-bold text-indigo-400 mb-8">
        Predict Emotion
      </h1>

      <div className="bg-slate-800 rounded-xl p-8 shadow-lg">

        <input
          type="file"
          accept="image/*"
          onChange={handleImage}
        />

        {preview && (
          <img
            src={preview}
            alt="preview"
            className="w-72 mt-6 rounded-lg shadow-lg"
          />
        )}

        <button
          onClick={handlePredict}
          disabled={loading}
          className="mt-8 bg-indigo-600 hover:bg-indigo-700 px-6 py-3 rounded-lg font-semibold"
        >
          {loading ? "Predicting..." : "Predict Emotion"}
        </button>

        {result && (
            <div className="mt-10 space-y-6">

            <div>
            <h2 className="text-2xl font-bold text-green-400">
             Emotion: {result.emotion}
            </h2>

        <p className="text-xl mt-2">
            Confidence: {result.confidence}%
        </p>
        </div>

        <div>
            <h3 className="text-xl font-semibold mb-3">
                Grad-CAM Visualization
            </h3>

      <img
        src={`http://127.0.0.1:8000/${result.gradcam_image.replace(/\\/g, "/")}`}
        alt="GradCAM"
        className="rounded-xl shadow-xl border border-slate-700 max-w-md"
      />
    </div>

  </div>
)}

      </div>

    </div>
  );
}

export default Predict;