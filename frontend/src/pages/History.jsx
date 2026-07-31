import { useEffect, useState } from "react";
import api from "../api/api";

function History() {
  const [predictions, setPredictions] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchHistory();
  }, []);

  const fetchHistory = async () => {
    try {
      const response = await api.get("/predictions");
      setPredictions(response.data);
    } catch (error) {
      console.error("Error fetching history:", error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="p-8 text-xl text-white">
        Loading prediction history...
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto p-8">
      <h1 className="text-4xl font-bold text-indigo-400 mb-8">
        Prediction History
      </h1>

      {predictions.length === 0 ? (
        <div className="bg-slate-800 rounded-xl p-8 text-center text-slate-300">
          No prediction history available.
        </div>
      ) : (
        <div className="overflow-x-auto rounded-xl shadow-lg">
          <table className="min-w-full bg-slate-800 text-white">
            <thead className="bg-slate-700">
              <tr>
                <th className="px-6 py-4 text-left">ID</th>
                <th className="px-6 py-4 text-left">Filename</th>
                <th className="px-6 py-4 text-left">Emotion</th>
                <th className="px-6 py-4 text-left">Confidence</th>
                <th className="px-6 py-4 text-left">Created At</th>
              </tr>
            </thead>

            <tbody>
              {predictions.map((item) => (
                <tr
                  key={item.id}
                  className="border-b border-slate-700 hover:bg-slate-700 transition"
                >
                  <td className="px-6 py-4">{item.id}</td>

                  <td className="px-6 py-4">
                    {item.filename}
                  </td>

                  <td className="px-6 py-4 font-semibold text-green-400">
                    {item.emotion}
                  </td>

                  <td className="px-6 py-4">
                    {item.confidence}%
                  </td>

                  <td className="px-6 py-4">
                    {new Date(item.created_at).toLocaleString()}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default History;