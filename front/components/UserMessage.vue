<template>
    <div
        v-if="message"
        id="user-message"
        :class="['user-message', message.type]"
    >
        {{ message.text }}
    </div>
</template>

<script>
/**
 * @type {Object} UserMessage
 * @property {string} text - The text of the message.
 * @property {string} type - The type of the message. Can be "success" or "error".
 */

/**
 * Vue component for displaying a user message.
 * @component
 *
 * @prop {string} text - The text content of the message.
 * @prop {string} type - The type of the message. Can be "success" or "error".
 *
 * @example
 * // In a Vue template:
 * <UserMessage ref="messageComponent"></UserMessage>
 *
 * // In a Vue method:
 * this.$refs.messageComponent.showMessage("Log in successful!", "success");
 */

export default {
    data() {
        return {
            /**
             * The message to display. This is an object with two properties:
             * - `text`: the text of the message
             * - `type`: the type of message, either "success" or "error"
             * @type {?UserMessage}
             */
            message: null,
        };
    },
    methods: {
        /**
         * Display a message to the user.
         * @param {string} text - The text of the message to display.
         * @param {string} type - The type of the message to display. Can be "success", "warning", or "error".
         */
        showMessage(text, type) {
            this.message = { text, type };
            setTimeout(() => {
                this.message = null;
            }, 5000);
        },
    },
};
</script>

<style lang="scss" scoped>
.user-message {
    position: absolute;
    top: 0;
    padding: 0.5rem 1rem;
    border-radius: 0.5rem;
    font-size: 1rem;
    font-weight: bold;
    margin: 1rem 0;
    font-family: "roboto" sans-serif;
}

.user-message.error {
    color: red;
    background-color: #fdecea;
}

.user-message.success {
    color: green;
    background-color: #d4edda;
}
</style>
