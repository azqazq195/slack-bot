from dataclasses import dataclass


@dataclass
class UserProfile:
    title: str
    phone: str
    skype: str
    real_name: str
    real_name_normalized: str
    display_name: str
    fields: str
    status_text: str
    status_emoji: str
    status_emoji_display_info: str
    status_expiration: str
    avatar_hash: str
    first_name: str
    last_name: str
    image_24: str
    image_32: str
    image_48: str
    image_72: str
    image_192: str
    image_512: str
    image_1024: str
    image_original: str
    status_text_canonical: str
    team: str
    display_name_normalized: str
    is_custom_image: bool


@dataclass
class User:
    id: str
    team_id: str
    name: str
    deleted: bool
    color: str
    real_name: str
    tz: str
    tz_label: str
    tz_offset: int
    is_admin: bool
    is_owner: bool
    is_primary_owner: bool
    is_restricted: bool
    is_ultra_restricted: bool
    is_bot: bool
    updated: int
    is_app_user: bool
    is_email_confirmed: bool
    who_can_share_contact_card: str
    profile: dict
