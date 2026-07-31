import { useEffect, useState } from "react";
import { Brain, BarChart3, Smile, Database } from "lucide-react";
import { Link } from "react-router-dom";
import api from "../api/api";

function Dashboard() {
  const [stats, setStats] =useState(null);
  const [recent, setRecent] = useState([]);

  useEffect(() => {
    fetchDashboard();
  }, []);

  const fetchDashboard = async () => {
    try {
      const statsRes = await api.get("/dashboard/stats");
      const historyRes = await api.get("/predictions");

      setStats(statsRes.data);
      setRecent(historyRes.data.slice(0, 5));
    } catch (err) {
      console.error(err);
    }
  };

  if (!stats) {
    return (
      <div className="p-8 text-white text-xl">
        Loading Dashboard...
      </div>
    );
  }

  const topEmotion = Object.keys(stats.emotion_counts)[0];

  return (
    <div className="max-w-7xl mx-auto p-8">

      <h1 className="text-5xl font-bold text-indigo-400 mb-10">
        EmotionSense AI Dashboard
      </h1>

      {/* Summary Cards */}

      <div className="grid md:grid-cols-2 xl:grid-cols-4 gap-6">

        <div className="bg-slate-800 rounded-xl p-6 shadow-lg">
          <Database className="text-indigo-400 mb-3" size={34} />

          <p className="text-slate-400">
            Total Predictions
          </p>

          <h2 className="text-4xl font-bold">
            {stats.total_predictions}
          </h2>
        </div>

        <div className="bg-slate-800 rounded-xl p-6 shadow-lg">
          <BarChart3 className="text-green-400 mb-3" size={34} />

          <p className="text-slate-400">
            Average Confidence
          </p>

          <h2 className="text-4xl font-bold">
            {stats.average_confidence}%
          </h2>
        </div>

        <div className="bg-slate-800 rounded-xl p-6 shadow-lg">
          <Smile className="text-yellow-400 mb-3" size={34} />

          <p className="text-slate-400">
            Top Emotion
          </p>

          <h2 className="text-4xl font-bold">
            {topEmotion}
          </h2>
        </div>

        <div className="bg-slate-800 rounded-xl p-6 shadow-lg">
          <Brain className="text-pink-400 mb-3" size={34} />

          <p className="text-slate-400">
            AI Model
          </p>

          <h2 className="text-2xl font-bold">
            CNN + Grad-CAM
          </h2>
        </div>

      </div>

      {/* Latest Prediction */}

      <div className="bg-slate-800 rounded-xl p-8 mt-10">

        <h2 className="text-2xl font-semibold mb-6">
          Latest Prediction
        </h2>

        <div className="space-y-3">

          <p>
            <strong>Filename:</strong>{" "}
            {stats.latest_prediction.filename}
          </p>

          <p>
            <strong>Emotion:</strong>{" "}
            {stats.latest_prediction.emotion}
          </p>

          <p>
            <strong>Confidence:</strong>{" "}
            {stats.latest_prediction.confidence}%
          </p>

          <p>
            <strong>Date:</strong>{" "}
            {new Date(
              stats.latest_prediction.created_at
            ).toLocaleString()}
          </p>

        </div>

      </div>

      {/* Quick Actions */}

      <div className="grid md:grid-cols-3 gap-6 mt-10">

        <Link
          to="/predict"
          className="bg-indigo-600 hover:bg-indigo-700 rounded-xl p-6 text-center text-xl font-semibold transition"
        >
          Upload Image
        </Link>

        <Link
          to="/history"
          className="bg-green-600 hover:bg-green-700 rounded-xl p-6 text-center text-xl font-semibold transition"
        >
          Prediction History
        </Link>

        <Link
          to="/analytics"
          className="bg-pink-600 hover:bg-pink-700 rounded-xl p-6 text-center text-xl font-semibold transition"
        >
          Analytics
        </Link>

      </div>

      {/* Recent Predictions */}

      <div className="bg-slate-800 rounded-xl p-8 mt-10">

        <h2 className="text-2xl font-semibold mb-6">
          Recent Predictions
        </h2>

        <table className="w-full">

          <thead>

            <tr className="text-left border-b border-slate-600">

              <th className="pb-3">Filename</th>

              <th className="pb-3">Emotion</th>

              <th className="pb-3">Confidence</th>

            </tr>

          </thead>

          <tbody>

            {recent.map((item) => (

              <tr
                key={item.id}
                className="border-b border-slate-700"
              >
                <td className="py-3">
                  {item.filename}
                </td>

                <td className="py-3 text-green-400">
                  {item.emotion}
                </td>

                <td className="py-3">
                  {item.confidence}%
                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>
  );
}

export default Dashboard;