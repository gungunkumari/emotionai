function About() {
  return (
    <div className="max-w-6xl mx-auto p-8">

      <h1 className="text-4xl font-bold text-indigo-400 mb-6">
        About EmotionSense AI
      </h1>

      {/* Project Overview */}
      <div className="bg-slate-800 rounded-xl p-6 mb-6 shadow-lg">
        <h2 className="text-2xl font-semibold mb-4 text-white">
          Project Overview
        </h2>

        <p className="text-slate-300 leading-8">
          EmotionSense AI is a Deep Learning-based facial emotion recognition
          system that predicts human emotions from facial images using a
          Convolutional Neural Network (CNN). The application also provides
          Grad-CAM visualization to explain the model's predictions, making
          the AI more transparent and understandable.
        </p>
      </div>

      {/* Features */}
      <div className="bg-slate-800 rounded-xl p-6 mb-6 shadow-lg">
        <h2 className="text-2xl font-semibold mb-4 text-white">
          Key Features
        </h2>

        <ul className="list-disc ml-6 text-slate-300 space-y-2">
          <li>Image Upload & Preview</li>
          <li>CNN-based Emotion Recognition</li>
          <li>Grad-CAM Explainability</li>
          <li>Prediction History</li>
          <li>Analytics Dashboard</li>
          <li>PostgreSQL Database Integration</li>
          <li>FastAPI REST APIs</li>
        </ul>
      </div>

      {/* Tech Stack */}
      <div className="bg-slate-800 rounded-xl p-6 mb-6 shadow-lg">
        <h2 className="text-2xl font-semibold mb-4 text-white">
          Technology Stack
        </h2>

        <div className="flex flex-wrap gap-3">
          {[
            "React",
            "Tailwind CSS",
            "FastAPI",
            "Python",
            "PyTorch",
            "CNN",
            "Grad-CAM",
            "PostgreSQL",
            "Axios",
            "Recharts",
          ].map((tech) => (
            <span
              key={tech}
              className="bg-indigo-600 px-4 py-2 rounded-full text-white"
            >
              {tech}
            </span>
          ))}
        </div>
      </div>

      {/* Developer */}
      <div className="bg-slate-800 rounded-xl p-6 mb-6 shadow-lg">
        <h2 className="text-2xl font-semibold mb-4 text-white">
          About the Developer
        </h2>

        <p className="text-slate-300 leading-8">
          <strong>Saanvi Kumari</strong> is a B.Tech Computer Science student
          specializing in Artificial Intelligence and Machine Learning. She is
          passionate about Deep Learning, Computer Vision, Full Stack
          Development, and building AI-powered applications that solve
          real-world problems.
        </p>
      </div>

      {/* Contact */}
      <div className="bg-slate-800 rounded-xl p-6 shadow-lg">
        <h2 className="text-2xl font-semibold mb-4 text-white">
          Contact Information
        </h2>

        <div className="space-y-3 text-slate-300">
          <p>
            📧 <strong>Email:</strong>{" "}
            <a
              href="mailto:saanvigungun2006@gmail.com"
              className="text-indigo-400 hover:underline"
            >
              saanvigungun2006@gmail.com
            </a>
          </p>

          <p>
            💻 <strong>GitHub:</strong>{" "}
            <a
              href="https://github.com/gungunkumari"
              target="_blank"
              rel="noopener noreferrer"
              className="text-indigo-400 hover:underline"
            >
              github.com/gungunkumari
            </a>
          </p>

          <p>
            💼 <strong>LinkedIn:</strong>{" "}
            <a
              href="https://www.linkedin.com/in/saanvi-kumari-4a3696295/"
              target="_blank"
              rel="noopener noreferrer"
              className="text-indigo-400 hover:underline"
            >
              linkedin.com/in/saanvi-kumari-4a3696295
            </a>
          </p>
        </div>
      </div>

    </div>
  );
}

export default About;