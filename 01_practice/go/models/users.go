package models

type User struct {
	gorm.Model
	Name string
	Sex  uint64
	Age  uint64
}
