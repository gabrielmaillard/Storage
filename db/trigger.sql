CREATE TRIGGER IF NOT EXISTS location_before_insert
BEFORE INSERT ON Locations
FOR EACH ROW
BEGIN
    SELECT
        CASE
            WHEN EXISTS (
                SELECT 1
                FROM Locations
                WHERE id = NEW.location_parent_id
            ) THEN
                RAISE(ABORT, 'Insertion annulée : location_parent_id référencé n''existe pas dans la table locations.')
            WHEN EXISTS (
                SELECT 1
                FROM Locations
                WHERE id = NEW.location_parent_id
                AND EXISTS (
                    SELECT 1
                    FROM Locations AS parent
                    WHERE parent.id = NEW.location_parent_id
                    AND parent.location_parent_id = NEW.id
                )
            ) THEN
                RAISE(ABORT, 'Insertion annulée : un location parent est déjà défini comme étant un descendant du location à insérer.')
        END;
END;
