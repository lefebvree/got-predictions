
<template>
  <div>
    <div class="columns">
      <div class="col-12 px-2">
        <div class="my-2 card panel-text">
          <h3><medal></medal> Room {{ room.name }}</h3>
          <p>
            Invite people to post their predictions in this room, each user can try to forecast what
            will happen this season and win or loose points with each answer.
          </p>
          <p>
            When a question gets answered in an episode it becomes locked and newcomers cannot bet points on it.
          </p>
          <p>
            <podium-gold></podium-gold> Total points display and rankings will be displayed here.
          </p>
        </div>
      </div>
      <div class="col-4 col-md-12 px-2">
        <div class="my-2 card panel-text">
          <h4><pencil-plus-outline class="mr-2"></pencil-plus-outline> Predictions</h4>
          <div v-if="userId !== null">
            <button class="btn btn-error m-2" @click="checkPredictions(userId)">
              <check-outline class="mr-2"></check-outline>
              See your Predictions
            </button>
          </div>
          <router-link :to="'/' + room.name + '/prediction'">
            <button class="btn btn-success m-2">
              <square-edit-outline class="mr-2"></square-edit-outline>
              Post new Predictions
            </button>
          </router-link>
        </div>
      </div>
      <div class="col-8 col-md-12 px-2">
        <div class="my-2 card panel-text">
          <h4><account-multiple-outline class="mr-2"></account-multiple-outline> Users</h4>
          <ul v-if="Object.keys(room.users).length > 0">
            <li v-for="(user, id) in room.users" :key="user.name">
              <span class="text-large pointer" @click="checkPredictions(id)">
                {{ user.name }}
                <book-open-page-variant class="ml-2"></book-open-page-variant>
              </span>
            </li>
          </ul>
          <p v-else>No one has posted any predictions yet, be the first one !</p>
        </div>
      </div>
    </div>
    <prediction-view ref="predictionsView"
      :userName="checkedUserName"
      :roomName="room.name"
      :predictionJson="checkedPredictions"
      :date="checkedDate"
    ></prediction-view>
  </div>
</template>

<script>

import PredictionView from '@/components/predictions/PredictionView.vue'

import AccountMultipleOutline from 'vue-material-design-icons/AccountMultipleOutline.vue'
import PencilPlusOutline from 'vue-material-design-icons/PencilPlusOutline.vue'
import BookOpenPageVariant from 'vue-material-design-icons/BookOpenPageVariant.vue'
import SquareEditOutline from 'vue-material-design-icons/SquareEditOutline.vue'
import CheckOutline from 'vue-material-design-icons/CheckOutline.vue'
import PodiumGold from 'vue-material-design-icons/PodiumGold.vue'
import Medal from 'vue-material-design-icons/Medal.vue'

export default {
  name: 'room',

  data () {
    return {
      refreshInterval: null,
      checkedUserName: '',
      checkedPredictions: '',
      checkedDate: ''
    }
  },

  computed: {
    room () {
      return this.$store.state.currentRoom
    },

    posted () {
      if (this.room.name in this.$store.state.savedRooms) {
        return this.$store.state.savedRooms[this.room.name].userName !== undefined
      } else {
        return false
      }
    },

    userId () {
      if (this.posted) {
        const userName = this.$store.state.savedRooms[this.room.name].userName
        const user = Object.entries(this.room.users).filter(([_, user]) => user.name === userName)

        return (user.length !== 0) ? user[0].id : null
      } else {
        return null
      }
    }
  },

  methods: {
    update () {
      this.$store.dispatch('updateRoom', this.room.name)
    },

    checkPredictions (userId) {
      const user = this.room.users[userId]
      this.checkedUserName = user.name
      this.checkedPredictions = user.predictions
      this.checkedDate = user.joined
      this.$refs.predictionsView.$el.classList.add('active')
    }
  },

  beforeMount () {
    this.$store.dispatch('updateRoom', this.$route.params.room)
    this.refreshInterval = window.setInterval(this.update, 1000)
  },

  beforeDestroy () {
    clearInterval(this.refreshInterval)
  },

  components: {
    AccountMultipleOutline,
    PencilPlusOutline,
    SquareEditOutline,
    CheckOutline,
    PodiumGold,
    Medal,
    PredictionView,
    BookOpenPageVariant
  }
}
</script>
