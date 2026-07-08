from uuid import UUID
import pytest

from study_manager.domain.models.user import User


class TestId:
    def test_should_generate_uuid_v7_when_id_is_not_provided(self) -> None:
        user = User(name="Test User", email="user@email.com")

        assert type(user.id) is UUID
        assert user.id.version == 7

    def test_should_reject_non_uuid_id(self) -> None:
        with pytest.raises(TypeError, match="Id must be a UUID"):
            User(
                name="Test User",
                email="user@email.com",
                user_id="INVALID ID",  # ty:ignore[invalid-argument-type]
            )

    def test_should_reject_invalid_uuid_version(self) -> None:
        user_id = UUID("550e8400-e29b-41d4-a716-446655440000")
        with pytest.raises(ValueError, match="Id must be a UUIDv7"):
            User(name="Test User", email="user@email.com", user_id=user_id)

    def test_should_preserve_given_valid_id(self) -> None:
        user_id = UUID("01943f7e-7c2b-7c0e-9f7b-2d5fd7a7a9d1")
        user = User(name="Test User", email="user@email.com", user_id=user_id)

        assert type(user.id) is UUID
        assert user.id.version == 7
        assert user.id == user_id

    def test_should_generate_different_ids_when_id_is_not_provided(self) -> None:
        user_dev = User(
            name="User Dev",
            email="user.dev@email.com",
        )
        user_dba = User(name="User DBA", email="user.dba@email.com")

        assert type(user_dev.id) is UUID
        assert type(user_dba.id) is UUID
        assert user_dev.id.version == 7
        assert user_dba.id.version == 7
        assert user_dev.id != user_dba.id


class TestName:
    def test_should_store_expected_value(self) -> None:
        user = User(name="Test User", email="user@email.com")

        assert user.name == "Test User"

    def test_should_strip_name_surrounding_whitespace(self) -> None:
        user = User(name="        Test User        ", email="user@email.com")

        assert user.name == "Test User"

    def test_should_reject_empty_name(self) -> None:
        with pytest.raises(ValueError, match="Name is required"):
            User(name="", email="user@email.com")

    def test_should_reject_blank_name(self) -> None:
        with pytest.raises(ValueError, match="Name is required"):
            User(name="                       ", email="user@email.com")

    def test_should_reject_non_string_name(self) -> None:
        with pytest.raises(TypeError, match="Name must be a string"):
            User(name=123, email="user@email.com")  # ty:ignore[invalid-argument-type]


class TestEmail:
    def test_should_store_expected_value(self) -> None:
        user = User(name="Test User", email="user@email.com")

        assert user.email == "user@email.com"

    def test_should_strip_email_surrounding_whitespace(self) -> None:
        user = User(name="Test User", email="        user@email.com        ")

        assert user.email == "user@email.com"

    def test_should_reject_empty_email(self) -> None:
        with pytest.raises(ValueError, match="Email is required"):
            User(name="Test User", email="")

    def test_should_reject_blank_email(self) -> None:
        with pytest.raises(ValueError, match="Email is required"):
            User(name="Test User", email="                       ")

    def test_should_reject_non_string_email(self) -> None:
        with pytest.raises(TypeError, match="Email must be a string"):
            User(
                name="Test User",
                email=123,  # ty:ignore[invalid-argument-type]
            )

    @pytest.mark.parametrize(
        "invalid_email",
        [
            "invalid-email",
            "useremail.com",
            "user@",
            "@email.com",
            "user@email",
            "user@@email.com",
        ],
    )
    def test_should_reject_invalid_email_format(self, invalid_email: str) -> None:
        with pytest.raises(
            ValueError,
            match="Email must be a valid email address",
        ):
            User(name="Test User", email=invalid_email)

    @pytest.mark.parametrize(
        "invalid_email",
        [
            123,
            True,
            object(),
        ],
    )
    def test_should_reject_not_string_email(self, invalid_email: object) -> None:
        with pytest.raises(TypeError, match="Email must be a string"):
            User(
                name="Test User",
                email=invalid_email,  # ty:ignore[invalid-argument-type]
            )
