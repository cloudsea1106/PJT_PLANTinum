<template>
  <div class="profile">
    <nav-bar></nav-bar>
    <div class="row mx-0">
      <!-- 여백 -->
      <div class="col-md-1 px-0 mx-0"></div>
      <!-- 내용 담을 흰 상자 -->
      <update-profile-detail class="col-md-10 mb-5 pb-5 px-0 mx-0"></update-profile-detail>
      <!-- 여백 -->
      <div class="col-md-1 px-0 mx-0"></div>
    </div>
  </div>
</template>

<script>
import UpdateProfileDetail from '@/components/UpdateProfileDetail.vue'
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'UpdateProfileView',
  components : {
    UpdateProfileDetail,
    NavBar
  }
}
</script>

<style scoped>
.profile {
  background-image: linear-gradient(rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.6)), url('@/assets/ProfileView/background_img.jpg');
  background-size: cover;
  height: 1000px;
}
</style>