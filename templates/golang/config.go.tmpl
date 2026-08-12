package config

import (
	"log"
	"os"

	"github.com/joho/godotenv"
	"go.uber.org/zap/zapcore"
)

var envLoaded = false

type Config struct {
	Port        string
	Environment string
}

type ZapConfig struct {
	LogLevel      zapcore.Level
	IsDevelopment bool
	Encoding      string
}

type DBConfig struct {
	DBUser     string
	DBPassword string
	DBHost     string
	DBPort     string
	DBName     string
}

// LoadEnv load's environment variables
func LoadEnv() {
	if envLoaded {
		return
	}

	if os.Getenv("GO_ENV") == "test" {
		envLoaded = true
		return
	}

	if err := godotenv.Load(); err != nil {
		log.Fatal("Failed to load .env file")
	}
	envLoaded = true
}

func Load() *Config {
	// setup
	LoadEnv()

	port := os.Getenv("PORT")
	if port == "" {
		log.Fatal("PORT environment variable is not set")
	}

	environment := os.Getenv("ENVIRONMENT")
	if environment == "" {
		log.Fatal("ENVIRONMENT environment variable is not set")
	}

	config := &Config{
		Port:        port,
		Environment: environment,
	}

	return config
}

// LoadDbConfig setup db config
func LoadDbConfig() *DBConfig {
	// setup
	LoadEnv()

	// gets db user if provided kills process with log.Fatal
	dbUser := os.Getenv("DB_USER")
	if dbUser == "" {
		log.Fatal("DB_USER environment variable is not set")
	}

	// gets db password if provided kills process with log.Fatal
	dbPassword := os.Getenv("DB_PASSWORD")
	if dbPassword == "" {
		log.Fatal("DB_PASSWORD environment variable is not set")
	}

	// gets db host if provided kills process with log.Fatal
	dbHost := os.Getenv("DB_HOST")
	if dbHost == "" {
		log.Fatal("DB_HOST environment variable is not set")
	}

	// gets db port if provided kills process with log.Fatal
	dbPort := os.Getenv("DB_PORT")
	if dbPort == "" {
		log.Fatal("DB_PORT environment variable is not set")
	}

	// gets db name if provided kills process with log.Fatal
	dbName := os.Getenv("DB_NAME")
	if dbName == "" {
		log.Fatal("DB_NAME environment variable is not set")
	}

	dbConfig := &DBConfig{
		DBUser:     dbUser,
		DBPassword: dbPassword,
		DBHost:     dbHost,
		DBPort:     dbPort,
		DBName:     dbName,
	}

	return dbConfig
}

// LoadZapConfig setup logger config
func LoadZapConfig() *ZapConfig {
	// setup
	LoadEnv()
	var config ZapConfig

	logLevel := os.Getenv("LOG_LEVEL")
	switch logLevel {
	case "DEBUG":
		config.LogLevel = zapcore.DebugLevel
		config.IsDevelopment = true
	case "INFO":
		config.LogLevel = zapcore.InfoLevel
		config.IsDevelopment = false
	default:
		config.LogLevel = zapcore.InfoLevel
		config.IsDevelopment = false
	}

	config.Encoding = "json"
	return &config
}
