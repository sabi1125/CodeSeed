package logger

import (
	"os"

	"go.uber.org/zap"
	"go.uber.org/zap/zapcore"
)

var log *zap.Logger

// Init initializes the logger from LOG_LEVEL and APP_ENV environment variables.
func Init() {
	var level zapcore.Level
	if err := level.UnmarshalText([]byte(os.Getenv("LOG_LEVEL"))); err != nil {
		level = zapcore.InfoLevel
	}

	isDevelopment := os.Getenv("APP_ENV") == "development"
	encoding := "json"
	if isDevelopment {
		encoding = "console"
	}

	encoderConfig := zapcore.EncoderConfig{
		TimeKey:        "timestamp",
		LevelKey:       "level",
		NameKey:        "logger",
		CallerKey:      "caller",
		MessageKey:     "message",
		StacktraceKey:  "stacktrace",
		LineEnding:     zapcore.DefaultLineEnding,
		EncodeLevel:    zapcore.CapitalLevelEncoder,
		EncodeTime:     zapcore.ISO8601TimeEncoder,
		EncodeDuration: zapcore.StringDurationEncoder,
		EncodeCaller:   zapcore.ShortCallerEncoder,
	}

	config := zap.Config{
		Level:            zap.NewAtomicLevelAt(level),
		Development:      isDevelopment,
		Encoding:         encoding,
		EncoderConfig:    encoderConfig,
		OutputPaths:      []string{"stdout"},
		ErrorOutputPaths: []string{"stderr"},
	}

	built, err := config.Build()
	if err != nil {
		panic("failed to build logger: " + err.Error())
	}

	log = built
}

// Get returns the underlying *zap.Logger, for callers that need direct access.
func Get() *zap.Logger {
	return log
}

// Sync flushes any buffered log entries — call before process exit.
func Sync() {
	log.Sync()
}

func Info(msg string, fields ...zap.Field) {
	log.Info(msg, fields...)
}

func Infow(msg string, fields ...interface{}) {
	log.Sugar().Infow(msg, fields...)
}

func Infof(templateString string, fields ...interface{}) {
	log.Sugar().Infof(templateString, fields...)
}

func Warn(msg string, fields ...zap.Field) {
	log.Warn(msg, fields...)
}

func Warnw(msg string, fields ...interface{}) {
	log.Sugar().Warnw(msg, fields...)
}

func Warnf(templateString string, fields ...interface{}) {
	log.Sugar().Warnf(templateString, fields...)
}

func Error(err error, fields ...zap.Field) {
	log.Error(err.Error(), fields...)
}

func Errorw(msg string, err error, fields ...interface{}) {
	log.Sugar().Errorw(msg, append(fields, "error", err.Error())...)
}

func Fatal(msg string, fields ...zap.Field) {
	log.Fatal(msg, fields...)
}

func Fatalf(templateString string, fields ...interface{}) {
	log.Sugar().Fatalf(templateString, fields...)
}

func Panic(msg string, fields ...zap.Field) {
	log.Panic(msg, fields...)
}

// InitForTest sets up a no-op logger for use in tests.
func InitForTest() {
	log = zap.NewNop()
}
