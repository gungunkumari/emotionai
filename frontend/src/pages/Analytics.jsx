import { useEffect, useState } from "react";
import api from "../api/api";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
} from "recharts";

function Analytics() {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    fetchStats();
  }, []);

  const fetchStats = async () => {
    try {
      const response = await api.get("/dashboard/stats");
      setStats(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  if (!stats) {
    return (
      <div className="p-8 text-xl text-white">
        Loading analytics...
      </div>
    );
  }

  const chartData = Object.entries(stats.emotion_counts).map(
    ([emotion, count]) => ({
      emotion,
      count,
    })
  );

  const COLORS = [
    "#6366F1",
    "#22C55E",
    "#F59E0B",
    "#EF4444",
    "#06B6D4",
    "#A855F7",
  ];

  return (
    <div className="max-w-7xl mx-auto p-8">

      <h1 className="text-4xl font-bold text-indigo-400 mb-8">
        Analytics Dashboard
      </h1>

      {/* Summary Cards */}

      <div className="grid md:grid-cols-3 gap-6 mb-10">

        <div className="bg-slate-800 rounded-xl p-6">
          <h2 className="text-slate-400">Total Predictions</h2>

          <p className="text-4xl font-bold mt-3">
            {stats.total_predictions}
          </p>
        </div>

        <div className="bg-slate-800 rounded-xl p-6">
          <h2 className="text-slate-400">Average Confidence</h2>

          <p className="text-4xl font-bold mt-3">
            {stats.average_confidence}%
          </p>
        </div>

        <div className="bg-slate-800 rounded-xl p-6">
          <h2 className="text-slate-400">Latest Emotion</h2>

          <p className="text-4xl font-bold mt-3 text-green-400">
            {stats.latest_prediction.emotion}
          </p>
        </div>

      </div>

      {/* Charts */}

      <div className="grid lg:grid-cols-2 gap-8">

        <div className="bg-slate-800 rounded-xl p-6 h-[420px]">
          <h2 className="text-xl font-semibold mb-6">
            Emotion Distribution
          </h2>

          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={chartData}>
              <XAxis dataKey="emotion" />
              <YAxis />
              <Tooltip />

              <Bar dataKey="count" fill="#6366F1" />
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div className="bg-slate-800 rounded-xl p-6 h-[420px]">
          <h2 className="text-xl font-semibold mb-6">
            Emotion Share
          </h2>

          <ResponsiveContainer width="100%" height="100%">
            <PieChart>

              <Pie
                data={chartData}
                dataKey="count"
                nameKey="emotion"
                outerRadius={120}
                label
              >
                {chartData.map((entry, index) => (
                  <Cell
                    key={entry.emotion}
                    fill={COLORS[index % COLORS.length]}
                  />
                ))}
              </Pie>

              <Tooltip />

            </PieChart>
          </ResponsiveContainer>

        </div>

      </div>

      {/* Latest Prediction */}

      <div className="mt-10 bg-slate-800 rounded-xl p-6">

        <h2 className="text-2xl font-semibold mb-6">
          Latest Prediction
        </h2>

        <div className="space-y-3">

          <p>
            <strong>Filename:</strong> {stats.latest_prediction.filename}
          </p>

          <p>
            <strong>Emotion:</strong> {stats.latest_prediction.emotion}
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

    </div>
  );
}

export default Analytics;