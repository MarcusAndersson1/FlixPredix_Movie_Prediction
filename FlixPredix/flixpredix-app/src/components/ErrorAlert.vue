<template>
<div>
    <v-alert v-model="alert" variant="tonal" closable close-label="Close Alert" color="red" title="Error!">
        Error when trying to generate score.</v-alert>

    <div v-if="!alert" class="text-center d-flex justify-space-around" >
        <v-btn @click="alert = true" color="red" variant="plain">
            Cancel
        </v-btn>
    </div>
</div>
</template>
<script>
  export default {
    data: () => ({
      alert: false,
    }),
    name: 'CancelButton',
    props: {
        msg: String
    }
  }
</script>