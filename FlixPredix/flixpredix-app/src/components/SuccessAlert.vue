<template>
<div>
    <v-alert v-model="alert" variant="tonal" closable close-label="Close Alert" color="success" title="Success!">
        The score would be: 10, I predict.</v-alert>

    <div v-if="!alert" class="text-center d-flex justify-space-around">
        <v-btn @click="alert = true" color="green" variant="plain">
            Generate
        </v-btn>
    </div>
</div>
</template>

    
<script>
export default {
    data: () => ({
        alert: false,
    }),
    name: 'GenerateButton',
    props: {
        msg: String
    },

     
}
</script>
