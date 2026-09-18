```flowchart
predictive_analysis> db.customers.aggregate([
| {
| $match:{
| churned:true
| }
| }
| ])
```
]
```flowchart
predictive_analysis> db.customers.aggregate([{
| $group:{
| _id:"$plan",
| total_customers:{$sum:1}
| }
| }])

```

​
