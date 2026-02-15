import Header from "./components/Header";
import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/category/") // Вставь свой API
      .then((res) => res.json())
      .then((data) => setCategories(data))
      .catch((err) => console.error("Ошибка при получении API:", err));
  }, []);

  return (
    <div style={{ fontFamily: "Arial" }}>
      {/* Шапка сайта */}
      <Header />

      {/* Основной контент */}
      <div style={{ padding: "20px" }}>
        <h1>Категории</h1>
        {categories.length === 0 ? (
          <p>Загрузка данных...</p>
        ) : (
          <ul>
            {categories.map((item) => (
              <li key={item.id}>{item.name}</li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}

export default App;
