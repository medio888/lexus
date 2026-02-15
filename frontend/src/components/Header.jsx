function Header() {
  return (
    <header id="header">
      <div id="header-content">
        <div id="header-content-logo">
          <img
            src="https://static.vecteezy.com/system/resources/previews/020/499/881/non_2x/lexus-brand-logo-car-symbol-black-design-japan-automobile-illustration-free-vector.jpg"
            alt="Lexus Logo"
          />
        </div>
        <nav id="header-content-category">
          <ul id="header-content-category-list">
            <li>Модели</li>
            <li>Автомобили с пробегом</li>
            <li>Специальные предложения</li>
            <li>Финансы и страхование</li>
            <li>Сервис</li>
            <li>Мир Lexus</li>
            <li>Записаться на тест-драйв</li>
          </ul>
        </nav>
        <div id="header-content-nambers">
          <p>0 (555) 02 43 89</p>
        </div>
        <div id="header-content-translator">
          <p>RU</p>
          <p>KG</p>
        </div>
        <div id="header-content-search">
          <input type="text" placeholder="Поиск по сайту" />
        </div>
      </div>
    </header>
  );
}

export default Header;