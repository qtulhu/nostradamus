import { createStore } from "vuex";

export default createStore({
    state () {
        return {
          values: null,
          response: {
              age: ['40-55 лет', '30-40 лет', '18-30 лет', '14-18 лет'],
          },
        }
      }
});
