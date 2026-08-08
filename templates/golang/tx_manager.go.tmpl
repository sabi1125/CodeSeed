package tx

import "context"

// Manager lets a caller run a function inside a single database transaction
// without that function needing to know about *gorm.DB directly. Lives in
// its own package so the domain layer (interactors) can depend on this
// interface without importing internal/infrastructure — same reasoning as
// the interactor/repository inputport split.
type Manager interface {
	WithinTransaction(ctx context.Context, fn func(ctx context.Context) error) error
}
