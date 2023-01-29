insert into doc_document_type(doc_type, description, is_accept_for_comments, is_accept_for_reactions, is_accept_for_tags, is_admin_level_only) 
values('news', 'Новости', true, true, true, false)

insert into doc_document_type(doc_type, description, is_accept_for_comments, is_accept_for_reactions, is_accept_for_tags, is_admin_level_only) 
values('project', 'Проект', true, true, true, false)

insert into doc_document_type(doc_type, description, is_accept_for_comments, is_accept_for_reactions, is_accept_for_tags, is_admin_level_only) 
values('idea', 'Идея для проекта', true, true, true, false)

insert into doc_document_type(doc_type, description, is_accept_for_comments, is_accept_for_reactions, is_accept_for_tags, is_admin_level_only) 
values('laboratory', 'Лаборатория', false, false, true, false)

insert into doc_document_type(doc_type, description, is_accept_for_comments, is_accept_for_reactions, is_accept_for_tags, is_admin_level_only) 
values('resume', 'Резюме', false, false, false, false)

insert into doc_document_type(doc_type, description, is_accept_for_comments, is_accept_for_reactions, is_accept_for_tags, is_admin_level_only) 
values('vacancy', 'Вакансия', false, false, false, false)

insert into doc_document_type(doc_type, description, is_accept_for_comments, is_accept_for_reactions, is_accept_for_tags, is_admin_level_only) 
values('lecturer', 'Преподаватель', false, false, true, false)

insert into doc_document_type(doc_type, description, is_accept_for_comments, is_accept_for_reactions, is_accept_for_tags, is_admin_level_only) 
values('graduate', 'Выпускник', false, false, true, false)

insert into usr_role(name, int_level)
values("USER", 1)

insert into usr_role(name, int_level)
values("SUPPORT", 2)

insert into usr_role(name, int_level)
values("MODERATOR", 3)

insert into usr_role(name, int_level)
values("ADMIN", 10000)