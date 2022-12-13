<template>
<body>
    <v-container>
        <v-row align-h="center">
            <v-col></v-col>
            <v-col align-h="center">
                <div id="titles">
                    <div id="titlecontent">
                        <p class="cred mx-auto" >FlixPredix</p>
						<br>
                        <span class="mx-auto"> Thank you for using FlixPredix, special thanks to our Team:
                            <br>
                            Carl Andreasson
                            <br>
                            Marcus Andersson
                            <br>
                            Felix Mertala
                            <br>
                            Adam Frison
                            <br>
                            Edvin Danielsson
                            <br>
                            Mislav Milicevic
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

</script>
<style>
.cred {
    font-family: "StWs";
    font-size: 100px;
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
    background-image: linear-gradient(top, rgba(0, 0, 0, 1) 0%, transparent 100%);
    pointer-events: none;
}

#titlecontent {
    position: absolute;
    top: 100%;
    animation: scroll 100s linear 4s infinite;
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
