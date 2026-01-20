---
name: mobile_developer
description: iOS and Android development expert. Covers Swift, Kotlin, SwiftUI, Jetpack Compose, React Native, Flutter, and app store guidelines.
---

# Mobile Developer Skill

Expert-level iOS and Android development for native and cross-platform apps.

## Model Selection for Mobile Tasks

| Task Type | Recommended Model | Why |
|-----------|-------------------|-----|
| **Complex architecture** | **Gemini 3 Pro** | System design, patterns |
| **UI/UX implementation** | **Claude Sonnet 4.5** | Creative, visual work |
| **Bug fixing** | **Claude Opus 4.5** | Deep debugging |
| **Quick code edits** | **Gemini 3 Flash** | Speed |

## When to Use This Skill

- Building native iOS apps (Swift, SwiftUI, UIKit)
- Building native Android apps (Kotlin, Jetpack Compose)
- Cross-platform development (React Native, Flutter)
- App Store / Play Store submission
- Performance optimization
- Push notifications, deep linking
- Local storage, CoreData, Room
- Networking, authentication

---

# PART 1: iOS DEVELOPMENT

## Swift/SwiftUI Patterns

### Project Structure

```
App/
├── App.swift              # @main entry point
├── Models/                # Data models
├── Views/                 # SwiftUI views
│   ├── Components/        # Reusable components
│   └── Screens/           # Full screens
├── ViewModels/            # MVVM view models
├── Services/              # API, database, etc.
├── Utilities/             # Extensions, helpers
└── Resources/             # Assets, localization
```

### SwiftUI Best Practices

```swift
// MVVM Pattern
class UserViewModel: ObservableObject {
    @Published var user: User?
    @Published var isLoading = false
    @Published var error: Error?
    
    private let userService: UserServiceProtocol
    
    init(userService: UserServiceProtocol = UserService()) {
        self.userService = userService
    }
    
    @MainActor
    func fetchUser() async {
        isLoading = true
        defer { isLoading = false }
        
        do {
            user = try await userService.getUser()
        } catch {
            self.error = error
        }
    }
}

// View using ViewModel
struct UserView: View {
    @StateObject private var viewModel = UserViewModel()
    
    var body: some View {
        Group {
            if viewModel.isLoading {
                ProgressView()
            } else if let user = viewModel.user {
                UserContent(user: user)
            } else if let error = viewModel.error {
                ErrorView(error: error)
            }
        }
        .task {
            await viewModel.fetchUser()
        }
    }
}
```

### UIKit Integration

```swift
// UIViewRepresentable for UIKit views in SwiftUI
struct MapViewRepresentable: UIViewRepresentable {
    @Binding var region: MKCoordinateRegion
    
    func makeUIView(context: Context) -> MKMapView {
        let mapView = MKMapView()
        mapView.delegate = context.coordinator
        return mapView
    }
    
    func updateUIView(_ mapView: MKMapView, context: Context) {
        mapView.setRegion(region, animated: true)
    }
    
    func makeCoordinator() -> Coordinator {
        Coordinator(self)
    }
    
    class Coordinator: NSObject, MKMapViewDelegate {
        var parent: MapViewRepresentable
        init(_ parent: MapViewRepresentable) {
            self.parent = parent
        }
    }
}
```

### Networking

```swift
// Modern async/await networking
protocol APIClient {
    func request<T: Decodable>(_ endpoint: Endpoint) async throws -> T
}

class URLSessionAPIClient: APIClient {
    private let session: URLSession
    private let decoder: JSONDecoder
    
    init(session: URLSession = .shared) {
        self.session = session
        self.decoder = JSONDecoder()
        self.decoder.keyDecodingStrategy = .convertFromSnakeCase
    }
    
    func request<T: Decodable>(_ endpoint: Endpoint) async throws -> T {
        let request = try endpoint.urlRequest()
        let (data, response) = try await session.data(for: request)
        
        guard let httpResponse = response as? HTTPURLResponse,
              200...299 ~= httpResponse.statusCode else {
            throw APIError.invalidResponse
        }
        
        return try decoder.decode(T.self, from: data)
    }
}
```

### Local Storage

```swift
// SwiftData (iOS 17+)
@Model
class Item {
    var name: String
    var timestamp: Date
    
    init(name: String, timestamp: Date = .now) {
        self.name = name
        self.timestamp = timestamp
    }
}

// CoreData for older iOS
class CoreDataStack {
    static let shared = CoreDataStack()
    
    lazy var persistentContainer: NSPersistentContainer = {
        let container = NSPersistentContainer(name: "Model")
        container.loadPersistentStores { _, error in
            if let error = error {
                fatalError("CoreData load failed: \(error)")
            }
        }
        return container
    }()
    
    var context: NSManagedObjectContext {
        persistentContainer.viewContext
    }
}
```

---

# PART 2: ANDROID DEVELOPMENT

## Kotlin/Jetpack Compose Patterns

### Project Structure

```
app/
├── src/main/
│   ├── java/com/example/app/
│   │   ├── MainActivity.kt
│   │   ├── di/                    # Dependency injection
│   │   ├── data/                  # Repository, data sources
│   │   │   ├── local/             # Room database
│   │   │   ├── remote/            # Retrofit API
│   │   │   └── repository/
│   │   ├── domain/                # Use cases, models
│   │   ├── ui/                    # Compose UI
│   │   │   ├── components/
│   │   │   ├── screens/
│   │   │   └── theme/
│   │   └── util/                  # Extensions, helpers
│   └── res/
└── build.gradle.kts
```

### Jetpack Compose Best Practices

```kotlin
// ViewModel with StateFlow
class UserViewModel(
    private val userRepository: UserRepository
) : ViewModel() {
    
    private val _uiState = MutableStateFlow<UserUiState>(UserUiState.Loading)
    val uiState: StateFlow<UserUiState> = _uiState.asStateFlow()
    
    init {
        fetchUser()
    }
    
    private fun fetchUser() {
        viewModelScope.launch {
            _uiState.value = UserUiState.Loading
            try {
                val user = userRepository.getUser()
                _uiState.value = UserUiState.Success(user)
            } catch (e: Exception) {
                _uiState.value = UserUiState.Error(e.message ?: "Unknown error")
            }
        }
    }
}

sealed class UserUiState {
    object Loading : UserUiState()
    data class Success(val user: User) : UserUiState()
    data class Error(val message: String) : UserUiState()
}

// Composable using ViewModel
@Composable
fun UserScreen(
    viewModel: UserViewModel = hiltViewModel()
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
    
    when (val state = uiState) {
        is UserUiState.Loading -> LoadingIndicator()
        is UserUiState.Success -> UserContent(user = state.user)
        is UserUiState.Error -> ErrorMessage(message = state.message)
    }
}
```

### Room Database

```kotlin
// Entity
@Entity(tableName = "users")
data class UserEntity(
    @PrimaryKey val id: String,
    val name: String,
    val email: String,
    @ColumnInfo(name = "created_at") val createdAt: Long
)

// DAO
@Dao
interface UserDao {
    @Query("SELECT * FROM users")
    fun getAllUsers(): Flow<List<UserEntity>>
    
    @Query("SELECT * FROM users WHERE id = :id")
    suspend fun getUserById(id: String): UserEntity?
    
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(user: UserEntity)
    
    @Delete
    suspend fun delete(user: UserEntity)
}

// Database
@Database(entities = [UserEntity::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao
}
```

### Networking with Retrofit

```kotlin
// API interface
interface ApiService {
    @GET("users/{id}")
    suspend fun getUser(@Path("id") id: String): UserDto
    
    @POST("users")
    suspend fun createUser(@Body user: CreateUserRequest): UserDto
    
    @GET("users")
    suspend fun getUsers(
        @Query("page") page: Int,
        @Query("limit") limit: Int
    ): UsersResponse
}

// Retrofit setup
object RetrofitClient {
    private val okHttpClient = OkHttpClient.Builder()
        .addInterceptor(HttpLoggingInterceptor().apply {
            level = HttpLoggingInterceptor.Level.BODY
        })
        .addInterceptor { chain ->
            val request = chain.request().newBuilder()
                .addHeader("Authorization", "Bearer ${TokenManager.token}")
                .build()
            chain.proceed(request)
        }
        .build()
    
    val api: ApiService = Retrofit.Builder()
        .baseUrl(BuildConfig.API_BASE_URL)
        .client(okHttpClient)
        .addConverterFactory(GsonConverterFactory.create())
        .build()
        .create(ApiService::class.java)
}
```

### Dependency Injection with Hilt

```kotlin
@Module
@InstallIn(SingletonComponent::class)
object AppModule {
    
    @Provides
    @Singleton
    fun provideDatabase(@ApplicationContext context: Context): AppDatabase {
        return Room.databaseBuilder(
            context,
            AppDatabase::class.java,
            "app_database"
        ).build()
    }
    
    @Provides
    fun provideUserDao(database: AppDatabase): UserDao {
        return database.userDao()
    }
    
    @Provides
    @Singleton
    fun provideApiService(): ApiService {
        return RetrofitClient.api
    }
}

@HiltViewModel
class UserViewModel @Inject constructor(
    private val userRepository: UserRepository
) : ViewModel() {
    // ...
}
```

---

# PART 3: CROSS-PLATFORM DEVELOPMENT

## React Native

### Project Structure

```
src/
├── components/          # Reusable components
├── screens/             # Screen components
├── navigation/          # React Navigation setup
├── hooks/               # Custom hooks
├── services/            # API, storage
├── store/               # Redux/Zustand state
├── utils/               # Helpers
└── theme/               # Colors, typography
```

### Best Practices

```typescript
// Custom hook for data fetching
function useUser(userId: string) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);
  
  useEffect(() => {
    let cancelled = false;
    
    async function fetchUser() {
      try {
        setLoading(true);
        const data = await api.getUser(userId);
        if (!cancelled) setUser(data);
      } catch (e) {
        if (!cancelled) setError(e as Error);
      } finally {
        if (!cancelled) setLoading(false);
      }
    }
    
    fetchUser();
    return () => { cancelled = true; };
  }, [userId]);
  
  return { user, loading, error };
}

// Screen component
function UserScreen({ route }: UserScreenProps) {
  const { userId } = route.params;
  const { user, loading, error } = useUser(userId);
  
  if (loading) return <LoadingSpinner />;
  if (error) return <ErrorView error={error} />;
  if (!user) return null;
  
  return (
    <ScrollView style={styles.container}>
      <UserProfile user={user} />
    </ScrollView>
  );
}
```

## Flutter

### Project Structure

```
lib/
├── main.dart
├── app/
│   ├── app.dart           # MaterialApp setup
│   └── routes.dart        # Route definitions
├── features/
│   └── user/
│       ├── data/          # Repository implementation
│       ├── domain/        # Entities, use cases
│       └── presentation/  # Widgets, BLoC/Provider
├── core/
│   ├── network/           # Dio client
│   ├── storage/           # SharedPreferences, Hive
│   └── theme/             # ThemeData
└── shared/
    └── widgets/           # Reusable widgets
```

### Best Practices

```dart
// State management with Riverpod
final userProvider = FutureProvider.family<User, String>((ref, userId) async {
  final repository = ref.watch(userRepositoryProvider);
  return repository.getUser(userId);
});

class UserScreen extends ConsumerWidget {
  final String userId;
  
  const UserScreen({required this.userId, super.key});
  
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final userAsync = ref.watch(userProvider(userId));
    
    return userAsync.when(
      loading: () => const Center(child: CircularProgressIndicator()),
      error: (error, stack) => ErrorWidget(error: error),
      data: (user) => UserContent(user: user),
    );
  }
}
```

---

# PART 4: APP STORE GUIDELINES

## iOS App Store

```markdown
REQUIREMENTS:
- App must provide value beyond a website
- No crashes or obvious bugs
- All features must work as described
- Privacy policy required
- App Tracking Transparency for tracking

COMMON REJECTIONS:
- Incomplete metadata or screenshots
- Broken links or placeholder content
- Guideline 4.2: Minimum functionality
- Guideline 2.1: App completeness
- Guideline 5.1.1: Data collection

SUBMISSION CHECKLIST:
- [ ] All app metadata complete
- [ ] Screenshots for all device sizes
- [ ] App preview video (optional but recommended)
- [ ] Privacy policy URL
- [ ] Support URL
- [ ] Test account if login required
- [ ] No TestFlight or debug code
```

## Google Play Store

```markdown
REQUIREMENTS:
- Target API level requirements (annually updated)
- 64-bit support required
- Privacy policy required
- Data safety section complete

COMMON ISSUES:
- Deceptive behavior
- Insufficient permissions justification
- Broken functionality
- Missing data safety information

SUBMISSION CHECKLIST:
- [ ] App bundle (.aab) not APK
- [ ] All store listing complete
- [ ] Screenshots for phone and tablet
- [ ] Privacy policy
- [ ] Data safety form complete
- [ ] Content rating questionnaire
- [ ] Tested on multiple devices/API levels
```

---

# PART 5: PERFORMANCE OPTIMIZATION

## iOS Performance

```markdown
MEMORY:
- Use weak/unowned to prevent retain cycles
- Implement didReceiveMemoryWarning
- Profile with Instruments (Allocations, Leaks)

RENDERING:
- Keep views simple
- Use LazyVStack/LazyHStack for lists
- Avoid expensive operations in body
- Profile with Instruments (Core Animation)

STARTUP:
- Defer non-essential initialization
- Use async loading for data
- Minimize app delegate work
```

## Android Performance

```markdown
MEMORY:
- Avoid memory leaks (ViewModel, WeakReference)
- Use lifecycle-aware components
- Profile with Android Studio Profiler

RENDERING:
- Use LazyColumn/LazyRow for lists
- Remember expensive calculations
- Avoid recomposition in hot paths
- Use Baseline Profiles

STARTUP:
- Initialize in background
- Use App Startup library
- Minimize Application.onCreate
```

---

# PART 6: COMMON PATTERNS

## Authentication Flow

```markdown
1. Check for existing token on launch
2. If valid, proceed to main app
3. If expired, attempt refresh
4. If no token or refresh failed, show login
5. After login, securely store tokens
6. Use Keychain (iOS) or EncryptedSharedPreferences (Android)
```

## Push Notifications

```markdown
iOS (APNs):
1. Request authorization (UNUserNotificationCenter)
2. Register for remote notifications
3. Handle deviceToken in AppDelegate
4. Send token to backend

Android (FCM):
1. Add Firebase dependencies
2. Create FirebaseMessagingService
3. Handle token refresh
4. Send token to backend
```

## Deep Linking

```markdown
iOS:
- Universal Links (preferred)
- Custom URL schemes (legacy)
- Handle in SceneDelegate or SwiftUI onOpenURL

Android:
- App Links (verified)
- Deep Links (unverified)
- Handle in Activity with intent-filter
- Use Navigation library for deep links
```

## Offline Support

```markdown
STRATEGY:
1. Cache API responses locally (Room/CoreData)
2. Show cached data immediately
3. Fetch fresh data in background
4. Update UI when new data arrives
5. Handle conflicts for write operations

TOOLS:
- iOS: URLCache, CoreData, SwiftData
- Android: Room, DataStore, OkHttp cache
```
