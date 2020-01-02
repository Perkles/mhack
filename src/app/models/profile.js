'use strict';
module.exports = (sequelize, DataTypes) => {
  const Profile = sequelize.define('Profile', {
    authenticationCode: DataTypes.STRING,
    userType: DataTypes.INTEGER
  }, {});
  Profile.associate = function(models) {
    // associations can be defined here
  };
  Profile.hasOne(User, {foreignKey: 'UserId', as: 'User'});
  return Profile;
};