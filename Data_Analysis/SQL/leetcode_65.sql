-- https://leetcode.com/problems/analyze-subscription-conversion/description/


SELECT user_id,
    ROUND((SUM(activity_duration) FILTER (WHERE activity_type = 'free_trial'))::DECIMAL / COUNT(*) FILTER (WHERE activity_type = 'free_trial'), 2) AS trial_avg_duration,
    ROUND((SUM(activity_duration) FILTER (WHERE activity_type = 'paid'))::DECIMAL / COUNT(*) FILTER (WHERE activity_type = 'paid'), 2) AS paid_avg_duration
    FROM useractivity
    GROUP BY user_id
    HAVING COUNT(*) FILTER (WHERE activity_type = 'paid') > 0
    ORDER BY user_id;