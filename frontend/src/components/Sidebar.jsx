import { NavLink } from "react-router-dom";
import {
  LayoutDashboard,
  Brain,
  History,
  BarChart3,
  Info,
} from "lucide-react";

function Sidebar() {
  const linkClass = ({ isActive }) =>
    `flex items-center gap-3 px-4 py-3 rounded-lg transition ${
      isActive
        ? "bg-indigo-600 text-white"
        : "text-slate-300 hover:bg-slate-700 hover:text-white"
    }`;

  return (
    <aside className="w-64 bg-slate-800 border-r border-slate-700 p-6">
      <h2 className="text-2xl font-bold text-indigo-400 mb-8">
        EmotionSense
      </h2>

      <nav className="space-y-2">
        <NavLink to="/" className={linkClass}>
          <LayoutDashboard size={20} />
          Dashboard
        </NavLink>

        <NavLink to="/predict" className={linkClass}>
          <Brain size={20} />
          Predict
        </NavLink>

        <NavLink to="/history" className={linkClass}>
          <History size={20} />
          History
        </NavLink>

        <NavLink to="/analytics" className={linkClass}>
          <BarChart3 size={20} />
          Analytics
        </NavLink>

        <NavLink to="/about" className={linkClass}>
          <Info size={20} />
          About
        </NavLink>
      </nav>
    </aside>
  );
}

export default Sidebar;