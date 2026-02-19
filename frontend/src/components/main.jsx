import GX from "./photo/GX_Lexus.webp";


function Main() {
    return (
        <main id="main">
            <div id="main-content">
                <section id="main-content-section-1">
                    <div id="main-content-section-1-image">
                        <img src={GX} alt="Lexus Gx Background"/>
                        </div>
                    <nav id="main-content-section-1-direction-1">
                        <a href="">Новый Lexus LX ➝</a>
                        <a href="">Новый Lexus NX ➝</a>
                        <a href="">Брошюры и прайс-листы ➝</a>
                        <a href="">Спецпредложения сервиса ➝</a>
                    </nav>
                    <nav id="main-content-section-1-direction-2">
                        <a href="">Обсолютно новый GX ⟶</a>
                    </nav>
                    <nav id="main-content-section-1-direction-3">
                        <a href=""><img src="" alt="" />Узнай о RX Hybrid</a>
                    </nav>
                </section>
                <section id="main-content-section-2"></section>
                <section id="main-content-section-3"></section>
                <section id="main-content-section-4"></section>
            </div>
        </main>
    );}

    export default Main;