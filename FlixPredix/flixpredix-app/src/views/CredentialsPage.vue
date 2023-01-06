<template>
<body>
    <v-container>
        <v-row align-h="center">
            <v-col></v-col>
            <v-col align-h="center">
                <div id="titles">
                    <div id="titlecontent">
                        <audio src="https://s.cdpn.io/1202/Star_Wars_original_opening_crawl_1977.mp3"></audio>
                        <h1 class="cred">FlixPredix</h1>
						<br>
                        <span class="mx-auto"> Thank you for using FlixPredix 
                            <br>
                            From all of us
                            <br>
                            <br>
                            Carl Skywalker
                            <br>
                            Marc Vader
                            <br>
                            Felix Fett
                            <br>
                            Adam Organa
                            <br>
                            Ed van Kenobi
                            <br>
                            Mislav Calrissian
                            <br>
                            <br>
                            Thanks!
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <br>
                            <h1 class="cred2">FlixPredix</h1>
                        </span>
                    </div>
                </div>
            </v-col>
            <v-col></v-col>
        </v-row>
    </v-container>
</body>
</template>
<script>
    var audio = new Audio('https://s.cdpn.io/1202/Star_Wars_original_opening_crawl_1977.mp3');
    audio.play();
</script>
<style>
.cred {
    font-family: "StWs";
    font-size: 100px;
    text-align: center;
}
.cred2 {
    font-family: "StWs";
    font-size: 145px;
    text-align: center;
}
#titles {
    position: absolute;
    width: 18em;
    height: 50em;
    bottom: 0;
    left: 50%;
    margin-left: -9em;
    font-size: 350%;
    font-weight: bold;
    text-align: justify;
    overflow: hidden;
    transform-origin: 50% 100%;
    transform: perspective(300px) rotateX(25deg);
}

#titles:after {
    position: absolute;
    content: ' ';
    left: 0;
    right: 0;
    top: 0;
    bottom: 60%;
    background-image: linear-gradient(to bottom, rgba(0, 0, 0, 1) 0%, transparent 100%);
    pointer-events: none;
}

#titlecontent {
    position: absolute;
    top: 100%;
    animation: scroll 100s linear 7s infinite;
}

@keyframes scroll {
    0% {
        top: 100%;
    }

    100% {
        top: -170%;
    }
}
</style>
