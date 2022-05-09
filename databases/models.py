from turtle import back
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String,Text
from sqlalchemy.orm import relationship,backref

from .database import Base


class User(Base):
    __tablename__ = "users"

    # user id 를 autoincrement and pk로 사용 // 
    id = Column(Integer, index=True, primary_key=True, unique=True, autoincrement=True)
    user_id = Column(String(255), index=True, primary_key=True, unique=True)
    hashed_password = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    is_active = Column(Boolean, default=True)

class Post(Base):
    __tablename__ = "posts"

    # 게시글 작성자 ID
    user_id = Column(ForeignKey('users.id'))
    # post 속성
    id = Column(Integer, index=True, primary_key=True, unique=True)
    title = Column(String(255), index=True)
    description = Column(Text())
    create_date = Column(DateTime(), nullable=False)

    # 정렬 기준 : create_date, User 테이블 역참조 시 users.get_user_post_id로 유저가 작성한 게시글을 참조할 수 있도록 하였음.
    post = relationship('User',backref=backref("get_user_post_id", order_by=create_date ))
    
class Comment(Base):
    __tablename__ = "comments"

    # 게시글 작성자 ID
    user_id = Column(ForeignKey('users.id'))
    # post ID
    post_id = Column(ForeignKey('posts.id',ondelete="CASCADE"))

    # comment 속성
    id = Column(Integer, index=True, primary_key=True, unique=True, autoincrement=True)
    comment_desc = Column(Text())
    create_date = Column(DateTime(), nullable=False)

    # 정렬 기준 : create_date, Post 테이블 역참조 시 posts.get_post_comment로 게시글에 대한 코멘트를 참조할 수 있도록 하였음.
    comment = relationship('Post',backref=backref("get_post_comment", order_by=create_date ))