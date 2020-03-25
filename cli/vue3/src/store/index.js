import Vue from 'vue'
import Vuex from 'vuex'
import {
  read,
  save
} from '../storage'
// 登录获取基础参数
// import confParameters from './modules/confParameters'

Vue.use(Vuex)
Vue.config.devtools = true
let modules = {
  // confParameters
}

// 刷新页面后把保存到stroage的数据还原到store中
let state = read('state') || '{}'
state = JSON.parse(state)
for (const key in state) {
  const obj = state[key] || modules[key].state
  modules[key].state = {
    ...obj
  }
}
save('state', '{}')

const store = new Vuex.Store({
  modules: modules,
  getters: {
  },
  mutations: {
  }
})

export default store
